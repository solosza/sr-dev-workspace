"""generate.py - Leaderboard page generator (generic, any topic).

A plain-English ranked list. Each idea shows: rank, name, a clear BUILD / TEST-FIRST /
DON'T-BUILD recommendation, one plain sentence, a small "how close to your world" tag,
and its OWN question box (ask about that idea; the answer appears right there).
Readable-first, no jargon, NO em dashes.

Usage: python generate.py <items_json_path> <session_dir>  ->  <session_dir>/page.html

Items JSON (topic-agnostic):
{ "title": str, "lead": str,
  "recLegend": [ {"label":str,"tone":"c|b|e"} ],       # optional, the rec key
  "legend": { "label": str, "tags": [ {"label":str,"tone":"a|b|c|d|e"} ] },
  "items": [ { "id":str, "rank":str, "name":str, "desc":str,
               "rec": {"label":"Build|Test first|Don't build","tone":"c|b|e"},
               "tag": {"label":str,"tone":"a|b|c|d|e"} } ] }
tone -> color: a=blue b=amber c=green d=grey e=red

Reply channel: the session answers a question by putting {ref, answer} on the status
reply's "answers" array; the page fills the matching pending answer inline.
"""
import html
import json
import os
import sys


def e(x):
    return html.escape(str(x))


def chip(t, cls="tag"):
    return f'<span class="{cls} t-{e(t.get("tone","d"))}">{e(t.get("label",""))}</span>' if t else ""


def item_html(it):
    iid = e(it["id"])
    return f"""<div class="row" id="row-{iid}">
  <div class="num">{e(it.get('rank',''))}</div>
  <div class="body">
    <div class="head"><span class="name">{e(it.get('name',''))}</span>{chip(it.get('rec'),'rec')}</div>
    <div class="desc">{e(it.get('desc',''))}</div>
    <div class="meta">{chip(it.get('tag'))}</div>
    <div class="qa" id="qa-{iid}"></div>
    <div class="askrow">
      <input class="ask" id="ask-{iid}" placeholder="ask a question about this..." onkeydown="if(event.key==='Enter')askItem('{iid}')">
      <button class="askbtn" onclick="askItem('{iid}')">Ask</button>
    </div>
  </div>
</div>"""


def build_page(d, sd):
    items = "".join(item_html(it) for it in d.get("items", []))
    lg = d.get("legend")
    legend = (f'<div class="key">{e(lg.get("label",""))} ' + "".join(chip(t) for t in lg.get("tags", [])) + "</div>") if lg else ""
    reclg = d.get("recLegend")
    reclegend = ('<div class="key">Recommendation: ' + "".join(chip(t, "rec") for t in reclg) + "</div>") if reclg else ""
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{e(d.get('title','Leaderboard'))}</title>
<style>
:root{{--ground:#fcfcfe;--panel:#f4f6fa;--ink:#1b1e26;--soft:#5c6479;--line:#e4e8f1;--accent:#2f6df0;
--a-bg:#eef3ff;--a-fg:#2f6df0;--b-bg:#fff2e2;--b-fg:#b9700a;--c-bg:#e9f7ee;--c-fg:#12924a;--d-bg:#eef0f4;--d-fg:#5c6479;--e-bg:#fdeef0;--e-fg:#c23a55;
--sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;--mono:ui-monospace,"SF Mono",Menlo,monospace;}}
@media(prefers-color-scheme:dark){{:root{{--ground:#0f1117;--panel:#181b22;--ink:#e9ebf1;--soft:#98a0b3;--line:#272c37;--accent:#6ea0ff;
--a-bg:#182338;--a-fg:#8fb4ff;--b-bg:#2a2110;--b-fg:#f0b757;--c-bg:#122a1c;--c-fg:#5fd08b;--d-bg:#20242e;--d-fg:#98a0b3;--e-bg:#2a1720;--e-fg:#f7849e;}}}}
:root[data-theme="light"]{{--ground:#fcfcfe;--panel:#f4f6fa;--ink:#1b1e26;--soft:#5c6479;--line:#e4e8f1;--accent:#2f6df0;--a-bg:#eef3ff;--a-fg:#2f6df0;--b-bg:#fff2e2;--b-fg:#b9700a;--c-bg:#e9f7ee;--c-fg:#12924a;--d-bg:#eef0f4;--d-fg:#5c6479;--e-bg:#fdeef0;--e-fg:#c23a55;}}
:root[data-theme="dark"]{{--ground:#0f1117;--panel:#181b22;--ink:#e9ebf1;--soft:#98a0b3;--line:#272c37;--accent:#6ea0ff;--a-bg:#182338;--a-fg:#8fb4ff;--b-bg:#2a2110;--b-fg:#f0b757;--c-bg:#122a1c;--c-fg:#5fd08b;--d-bg:#20242e;--d-fg:#98a0b3;--e-bg:#2a1720;--e-fg:#f7849e;}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--ground);color:var(--ink);font-family:var(--sans);line-height:1.55;padding:2rem clamp(1rem,5vw,2rem)}}
.wrap{{max-width:46rem;margin:0 auto}}
.banner{{font-size:.75rem;color:var(--soft);margin-bottom:1rem;word-break:break-all}}
h1{{font-size:clamp(1.5rem,4vw,2.05rem);font-weight:700;letter-spacing:-.02em;text-wrap:balance}}
.lead{{color:var(--soft);font-size:1.02rem;margin-top:.5rem;max-width:38rem}}
.key{{display:flex;flex-wrap:wrap;gap:.5rem .8rem;align-items:center;margin:.9rem 0 0;font-size:.82rem;color:var(--soft)}}
.tag{{font-size:.74rem;font-weight:650;padding:.2rem .55rem;border-radius:1rem;white-space:nowrap}}
.rec{{font-size:.74rem;font-weight:700;padding:.2rem .6rem;border-radius:.4rem;white-space:nowrap}}
.t-a{{background:var(--a-bg);color:var(--a-fg)}} .t-b{{background:var(--b-bg);color:var(--b-fg)}} .t-c{{background:var(--c-bg);color:var(--c-fg)}} .t-d{{background:var(--d-bg);color:var(--d-fg)}} .t-e{{background:var(--e-bg);color:var(--e-fg)}}
.strip{{display:flex;align-items:center;gap:.5rem;font-size:.76rem;color:var(--soft);margin:1rem 0 .5rem}}
.dot{{width:.5rem;height:.5rem;border-radius:50%;background:var(--soft);display:inline-block}} .dot-processing{{background:var(--accent);animation:p 1.2s infinite}} @keyframes p{{0%,100%{{opacity:1}}50%{{opacity:.4}}}}
.row{{display:grid;grid-template-columns:2.6rem 1fr;gap:.2rem 1rem;align-items:start;padding:1.25rem .2rem;border-top:1px solid var(--line)}}
.row:first-of-type{{border-top:2px solid var(--ink)}}
.num{{font-family:var(--mono);font-size:1.5rem;font-weight:700;color:var(--soft);font-variant-numeric:tabular-nums;line-height:1.3}}
.row:nth-of-type(-n+3) .num{{color:var(--accent)}}
.head{{display:flex;align-items:center;gap:.6rem;flex-wrap:wrap;margin-bottom:.15rem}}
.name{{font-size:1.12rem;font-weight:650;line-height:1.3;text-wrap:balance}}
.desc{{color:var(--soft);font-size:.95rem;max-width:36rem}}
.meta{{margin-top:.5rem}}
.qa{{margin-top:.55rem}} .qa .item{{margin-top:.5rem;font-size:.9rem;border-left:2px solid var(--line);padding-left:.7rem}}
.qa .q{{font-weight:600}} .qa .a{{color:var(--soft);margin-top:.15rem;white-space:pre-wrap}} .qa .pending{{font-style:italic;opacity:.7}}
.askrow{{display:flex;gap:.5rem;margin-top:.6rem;max-width:34rem}}
.ask{{flex:1;border:1px solid var(--line);border-radius:.5rem;padding:.45rem .65rem;font-size:.88rem;background:var(--panel);color:var(--ink)}}
.ask:focus{{outline:none;border-color:var(--accent)}}
.askbtn{{background:var(--accent);color:#fff;border:none;border-radius:.5rem;padding:.45rem 1rem;font-size:.85rem;font-weight:600;cursor:pointer}}
@media(max-width:36rem){{.row{{grid-template-columns:2.2rem 1fr}}}}
</style></head><body><div class="wrap">
<div class="banner"><b>Session:</b> {e(sd)}</div>
<h1>{e(d.get('title','Leaderboard'))}</h1>
<p class="lead">{e(d.get('lead',''))}</p>
{reclegend}{legend}
<div class="strip"><span class="dot" id="dot"></span><span id="slabel">idle</span> &nbsp; ask a question on any idea; the answer appears right under it.</div>
{items}
</div>
<script>
async function askItem(id){{var inp=document.getElementById('ask-'+id);var q=inp.value.trim();if(!q)return;inp.value='';var ref='q'+Date.now();var el=document.createElement('div');el.className='item';el.id=ref;el.innerHTML='<div class="q">'+q.replace(/</g,'&lt;')+'</div><div class="a pending">thinking...</div>';document.getElementById('qa-'+id).appendChild(el);try{{await fetch('/annotate',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{target:String(id),action:'ask',raw_words:q,ref:ref,at:new Date().toISOString()}})}});}}catch(e){{}}}}
async function poll(){{var d;try{{d=await (await fetch('/status')).json();}}catch(e){{d={{status:'idle'}};}}var s=(d&&d.status)||'idle';document.getElementById('dot').className='dot dot-'+s;document.getElementById('slabel').textContent=s;var ans=(d&&d.answers)||[];for(var i=0;i<ans.length;i++){{var el=document.getElementById(ans[i].ref);if(el){{var a=el.querySelector('.a');if(a&&a.classList.contains('pending')){{a.classList.remove('pending');a.textContent=ans[i].answer||'';}}}}}}}}
poll();setInterval(poll,2000);
</script></body></html>"""


def main():
    if len(sys.argv) != 3:
        print("Usage: python generate.py <items_json_path> <session_dir>", file=sys.stderr)
        sys.exit(1)
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        data = json.load(f)
    sd = os.path.abspath(sys.argv[2])
    with open(os.path.join(sd, "page.html"), "w", encoding="utf-8") as f:
        f.write(build_page(data, sd))
    print("Written: " + os.path.join(sd, "page.html"))


if __name__ == "__main__":
    main()
