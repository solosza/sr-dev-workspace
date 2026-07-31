"""generate.py - Venture-board page generator (kanban format, permanent).

Renders venture-loop ideas as a KANBAN: a summary funnel on top, stage columns,
verdict cards with a fit tag (low/cond/high), signal chips, a per-card note and
OK/Hold/Redirect buttons, a legend, and a general-comments field. The board is a
capture surface - buttons POST to /annotate; /status is polled for results.

Usage: python generate.py <items_json_path> <session_dir>  ->  <session_dir>/page.html

Items JSON:
{ "title": str, "subtitle": str,
  "funnel": [ {"label":str,"value":int|str,"tone":"go|kill|none","wide":bool} ],
  "columns": [str],
  "cards": [ {"id":str,"title":str,"column":str,"verdict":"GO|GO-IF|KILL|PARK|-",
              "fit":"low|cond|high|-","signals":[str],"summary":str,"take":str,
              "rank":str?,"subtext":str?} ] }
"""
import html
import json
import os
import sys

VC = {"GO": "go", "GO-IF": "goif", "KILL": "kill", "PARK": "park"}


def e(x):
    return html.escape(str(x))


def card_html(c):
    cid = e(c["id"])
    verdict = str(c.get("verdict", "-")).upper()
    vcls = VC.get(verdict, "park")
    rank = f'<span class="rk">{e(c["rank"])}</span>' if c.get("rank") else ""
    fit = str(c.get("fit", "")).lower()
    fitt = f'<span class="fit fit-{fit}">fit: {e(fit)}</span>' if fit and fit != "-" else ""
    pill = f'<span class="pill pill-{vcls}">{e(verdict)}</span>' if verdict != "-" else ""
    sig = "".join(f'<span class="chip">{e(s)}</span>' for s in c.get("signals", []))
    sub = f'<p class="subtext">{e(c["subtext"])}</p>' if c.get("subtext") else ""
    take = f'<p class="take">Next: {e(c["take"])}</p>' if c.get("take") else ""
    return f"""<div class="card {vcls}" id="card-{cid}">
  <div class="chd">{rank}{pill}<span class="ct">{e(c.get('title',''))}</span>{fitt}</div>
  <div class="chips">{sig}</div>
  <p class="csum">{e(c.get('summary',''))}</p>{sub}{take}
  <textarea id="note-{cid}" class="note" rows="1" placeholder="note (verbatim into the kernel)"></textarea>
  <div class="acts">
    <button class="btn ok" onclick="act('{cid}','ok')">&#128077; Deeper</button>
    <button class="btn hold" onclick="act('{cid}','hold')">&#9208; Hold</button>
    <button class="btn rd" onclick="act('{cid}','redirect')">&#8597; Redirect</button>
  </div>
</div>"""


def build_page(d, sd):
    cards = d.get("cards", [])
    cols = d.get("columns") or sorted({c.get("column", "Ideas") for c in cards})
    by = {n: [c for c in cards if c.get("column", cols[0]) == n] for n in cols}
    funnel = "".join(
        f'<div class="fstat {("go" if f.get("tone")=="go" else "kill" if f.get("tone")=="kill" else "")} {("wide" if f.get("wide") else "")}">'
        f'<span class="k">{e(f["value"])}</span> {e(f["label"])}</div>'
        for f in d.get("funnel", []))
    columns = "".join(
        f'<div class="col"><div class="colh">{e(n)}<span class="cc">{len(by[n])}</span></div>'
        + ("".join(card_html(c) for c in by[n]) or '<div class="empty">-</div>') + "</div>"
        for n in cols)
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{e(d.get('title','Venture Board'))}</title>
<style>
:root{{--ground:#fbfbfd;--panel:#f2f4f8;--panel2:#e9edf4;--ink:#191c22;--muted:#697086;--line:#e1e6f0;--accent:#2563eb;
--go:#15a34a;--goif:#c26a08;--kill:#d63a3a;--park:#7b8496;
--low-bg:#fbeef0;--low-fg:#c23a55;--cond-bg:#fbf1e3;--cond-fg:#c26a08;--high-bg:#e9f7ee;--high-fg:#15a34a;
--mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;--sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;}}
@media(prefers-color-scheme:dark){{:root{{--ground:#111319;--panel:#1a1d25;--panel2:#20242e;--ink:#e7e9f0;--muted:#8b93a6;--line:#2a2f3b;--accent:#6c9bff;
--go:#4ade80;--goif:#fbbf24;--kill:#f87171;--park:#9aa3b5;
--low-bg:#2a1720;--low-fg:#f7849e;--cond-bg:#2a2010;--cond-fg:#fbbf24;--high-bg:#12271b;--high-fg:#4ade80;}}}}
:root[data-theme="light"]{{--ground:#fbfbfd;--panel:#f2f4f8;--panel2:#e9edf4;--ink:#191c22;--muted:#697086;--line:#e1e6f0;--accent:#2563eb;--go:#15a34a;--goif:#c26a08;--kill:#d63a3a;--park:#7b8496;--low-bg:#fbeef0;--low-fg:#c23a55;--cond-bg:#fbf1e3;--cond-fg:#c26a08;--high-bg:#e9f7ee;--high-fg:#15a34a;}}
:root[data-theme="dark"]{{--ground:#111319;--panel:#1a1d25;--panel2:#20242e;--ink:#e7e9f0;--muted:#8b93a6;--line:#2a2f3b;--accent:#6c9bff;--go:#4ade80;--goif:#fbbf24;--kill:#f87171;--park:#9aa3b5;--low-bg:#2a1720;--low-fg:#f7849e;--cond-bg:#2a2010;--cond-fg:#fbbf24;--high-bg:#12271b;--high-fg:#4ade80;}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--ground);color:var(--ink);font-family:var(--sans);line-height:1.5;padding:1.5rem clamp(1rem,4vw,2.5rem)}}
.banner{{max-width:80rem;margin:0 auto .75rem;font-size:.76rem;color:var(--muted);word-break:break-all}}
.head{{max-width:80rem;margin:0 auto}}
.eyebrow{{font-family:var(--mono);font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);margin-bottom:.35rem}}
h1{{font-size:clamp(1.35rem,3vw,1.9rem);font-weight:680;letter-spacing:-.01em;text-wrap:balance}}
.sub{{color:var(--muted);font-size:.94rem;margin-top:.2rem;max-width:64ch}}
.funnel{{max-width:80rem;margin:1rem auto;display:flex;flex-wrap:wrap;gap:.6rem}}
.fstat{{background:var(--panel);border:1px solid var(--line);border-radius:.65rem;padding:.6rem .95rem;font-size:.82rem}}
.fstat .k{{font-family:var(--mono);font-weight:700;font-variant-numeric:tabular-nums;font-size:1.15rem}}
.fstat.go .k{{color:var(--go)}} .fstat.kill .k{{color:var(--kill)}}
.fstat.wide{{flex:1 1 20rem}} .fstat.wide .k{{color:var(--goif);font-size:.82rem}}
.legend{{max-width:80rem;margin:0 auto 1rem;font-size:.8rem;color:var(--muted)}} .legend b{{color:var(--ink)}}
.strip{{max-width:80rem;margin:0 auto .8rem;display:flex;align-items:center;gap:.5rem;font-size:.78rem;color:var(--muted)}}
.dot{{width:.5rem;height:.5rem;border-radius:50%;background:var(--muted);display:inline-block}} .dot-processing{{background:var(--accent);animation:p 1.2s infinite}} @keyframes p{{0%,100%{{opacity:1}}50%{{opacity:.4}}}}
.board{{max-width:100%;overflow-x:auto;padding-bottom:1rem}}
.cols{{display:flex;gap:.9rem;min-width:min-content;max-width:80rem;margin:0 auto}}
.col{{flex:0 0 18rem;width:18rem}}
.colh{{font-family:var(--mono);font-size:.74rem;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);padding:.25rem .1rem .55rem;border-bottom:2px solid var(--line);margin-bottom:.7rem;display:flex;align-items:center;gap:.4rem}}
.cc{{margin-left:auto;background:var(--panel2);border-radius:1rem;padding:.05rem .5rem;font-size:.7rem;font-weight:700;color:var(--ink)}}
.empty{{color:var(--muted);font-size:.8rem;padding:.4rem .1rem;font-style:italic}}
.card{{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--stripe,var(--park));border-radius:.6rem;padding:.75rem;margin-bottom:.65rem;transition:opacity .2s}}
.card.go{{--stripe:var(--go)}} .card.goif{{--stripe:var(--goif)}} .card.kill{{--stripe:var(--kill)}} .card.park{{--stripe:var(--park)}} .card.acted{{opacity:.5}}
.chd{{display:flex;align-items:center;gap:.4rem;margin-bottom:.4rem;flex-wrap:wrap}}
.rk{{font-family:var(--mono);font-weight:700;color:var(--accent);font-size:.8rem}}
.ct{{font-size:.9rem;font-weight:620;line-height:1.25;flex:1 1 auto;min-width:8rem;text-wrap:balance}}
.pill{{font-family:var(--mono);font-size:.62rem;font-weight:700;padding:.14rem .45rem;border-radius:.35rem;color:#fff;white-space:nowrap}}
.pill-go{{background:var(--go)}}.pill-goif{{background:var(--goif)}}.pill-kill{{background:var(--kill)}}.pill-park{{background:var(--park)}}
.fit{{font-family:var(--mono);font-size:.62rem;font-weight:700;padding:.12rem .42rem;border-radius:.32rem;white-space:nowrap}}
.fit-low{{background:var(--low-bg);color:var(--low-fg)}} .fit-cond{{background:var(--cond-bg);color:var(--cond-fg)}} .fit-high{{background:var(--high-bg);color:var(--high-fg)}}
.chips{{display:flex;gap:.3rem;flex-wrap:wrap;margin-bottom:.4rem}}
.chip{{font-size:.68rem;padding:.1rem .42rem;border-radius:1rem;background:var(--panel2);color:var(--muted);border:1px solid var(--line)}}
.csum{{font-size:.79rem;line-height:1.45;margin-bottom:.35rem}} .subtext{{font-size:.72rem;color:var(--muted);font-style:italic;margin-bottom:.4rem}}
.take{{font-family:var(--mono);font-size:.72rem;color:var(--accent);margin-bottom:.5rem}}
.note{{width:100%;border:1px solid var(--line);border-radius:.35rem;padding:.35rem;font-size:.76rem;background:var(--ground);color:var(--ink);resize:vertical;margin-bottom:.45rem}}
.acts{{display:flex;gap:.3rem;flex-wrap:wrap}}
.btn{{border:1px solid var(--line);padding:.3rem .55rem;border-radius:.4rem;font-size:.72rem;font-weight:600;cursor:pointer;background:var(--panel2);color:var(--ink)}} .btn:hover{{filter:brightness(1.05)}} .btn:disabled{{opacity:.4;cursor:default}}
.btn.ok{{background:color-mix(in srgb,var(--go) 16%,var(--panel2));border-color:color-mix(in srgb,var(--go) 40%,transparent)}}
.btn.rd{{background:color-mix(in srgb,var(--goif) 16%,var(--panel2));border-color:color-mix(in srgb,var(--goif) 40%,transparent)}}
.general{{max-width:80rem;margin:1.25rem auto .5rem}} .general label{{display:block;font-size:.8rem;color:var(--muted);margin-bottom:.3rem}}
.general textarea{{width:100%;border:1px solid var(--line);border-radius:.375rem;padding:.55rem;font-size:.9rem;background:var(--panel);color:var(--ink);resize:vertical}}
.sendbar{{position:sticky;bottom:0;max-width:80rem;margin:0 auto;background:var(--ground);border-top:1px solid var(--line);padding:.7rem 0;display:flex;align-items:center;gap:1rem}}
#send{{background:var(--accent);color:#fff;border:none;padding:.5rem 1.2rem;border-radius:.375rem;font-size:.9rem;font-weight:600;cursor:pointer}} #send:disabled{{opacity:.5}}
.count,#status{{font-size:.83rem;color:var(--muted)}}
.res{{margin-top:.4rem;padding:.35rem .6rem;border-radius:.35rem;font-size:.76rem;font-weight:600;background:var(--accent);color:#fff}}
</style></head><body>
<div class="banner"><b>Session:</b> {e(sd)}</div>
<div class="head"><div class="eyebrow">Venture Board</div><h1>{e(d.get('title','Venture Board'))}</h1><div class="sub">{e(d.get('subtitle',''))}</div></div>
<div class="funnel">{funnel}</div>
<div class="strip"><span class="dot" id="dot"></span><span id="slabel">idle</span></div>
<div class="legend"><b>fit</b>: <span class="fit fit-low">low</span> not you · <span class="fit fit-cond">cond</span> partial · <span class="fit fit-high">high</span> yours (a tag, never a ranker) &nbsp;·&nbsp; &#128077; <b>Deeper</b> = run the next loop · &#9208; <b>Hold</b> = park · &#8597; <b>Redirect</b> = your note steers it. Columns = pipeline stage.</div>
<div class="board"><div class="cols">{columns}</div></div>
<div class="general"><label>General comments (whole board):</label><textarea id="gc" rows="2" placeholder="session-wide input - rides the submit"></textarea></div>
<div class="sendbar"><button id="send" onclick="sendAll()">Send to session</button><span class="count" id="qc">0 queued</span><span id="status"></span></div>
<script>
var queue={{}};
function act(id,a){{var t=document.getElementById('note-'+id);queue[id]={{target:String(id),action:a,raw_words:(t&&t.value.trim())||null,at:new Date().toISOString()}};var c=document.getElementById('card-'+id);c.classList.add('acted');var b=c.querySelectorAll('.btn');for(var i=0;i<b.length;i++)b[i].disabled=true;document.getElementById('qc').textContent=Object.keys(queue).length+' queued';}}
async function sendAll(){{document.getElementById('send').disabled=true;var k=Object.keys(queue),s=0,er=0;for(var i=0;i<k.length;i++){{try{{var r=await fetch('/annotate',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify(queue[k[i]])}});r.ok?s++:er++;}}catch(e){{er++;}}}}var g=document.getElementById('gc').value.trim();try{{await fetch('/annotate',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{target:'__session__',action:'submit',raw_words:g||null,at:new Date().toISOString()}})}});s++;}}catch(e){{er++;}}queue={{}};document.getElementById('qc').textContent='0 queued';document.getElementById('status').textContent=s+' sent'+(er?', '+er+' failed':'');}}
async function poll(){{var d;try{{d=await (await fetch('/status')).json();}}catch(e){{d={{status:'idle'}};}}var s=(d&&d.status)||'idle';document.getElementById('dot').className='dot dot-'+s;document.getElementById('slabel').textContent=s;var rs=(d&&d.results)||[];for(var i=0;i<rs.length;i++){{var t=rs[i].target,c=document.getElementById('card-'+t);if(c&&!document.getElementById('res-'+t)){{var x=document.createElement('div');x.id='res-'+t;x.className='res';x.textContent='-> '+(rs[i].outcome||'done');c.appendChild(x);c.classList.add('acted');}}}}}}
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
