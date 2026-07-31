"""generate.py - Venture-board page generator (pipeline / kanban format).

Renders venture-loop ideas as cards grouped into pipeline STAGE COLUMNS, with a
summary FUNNEL bar on top (the biggest element), a legend, per-card
OK/Hold/Redirect + note, and a general-comments field. Format follows dashboard
best practice: summary hierarchy up top, kanban workflow view, scoring on cards.

Usage: python generate.py <items_json_path> <session_dir>  ->  <session_dir>/page.html

Items JSON:
{ "title": str, "subtitle": str,
  "funnel": [ {"label": str, "value": int|str} ],          # big summary stats
  "columns": [str],                                          # ordered stage names
  "cards": [ { "id": str, "title": str, "column": str,
               "verdict": "GO|GO-IF|KILL|PARK|-",
               "signals": [str], "fit": "high|cond|low|-",
               "summary": str, "take": str } ] }
"""
import html
import json
import os
import sys

VCLASS = {"GO": "go", "GO-IF": "goif", "KILL": "kill", "PARK": "park"}


def esc(x):
    return html.escape(str(x))


def card_html(c):
    cid = esc(c["id"])
    verdict = str(c.get("verdict", "-")).upper()
    vcls = VCLASS.get(verdict, "none")
    sig = "".join(f'<span class="chip">{esc(s)}</span>' for s in c.get("signals", []))
    fit = str(c.get("fit", "")).lower()
    fitchip = f'<span class="chip chip-fit-{fit}">fit: {esc(fit)}</span>' if fit and fit != "-" else ""
    take = f'<p class="take">Next: {esc(c["take"])}</p>' if c.get("take") else ""
    return f"""<div class="card" id="card-{cid}">
  <div class="chd"><span class="pill pill-{vcls}">{esc(verdict)}</span><span class="ctitle">{esc(c.get('title',''))}</span></div>
  <div class="chips">{fitchip}{sig}</div>
  <p class="csum">{esc(c.get('summary',''))}</p>{take}
  <textarea id="note-{cid}" class="note" rows="1" placeholder="note (verbatim)"></textarea>
  <div class="acts">
    <button class="btn btn-ok" onclick="act('{cid}','ok')">&#128077; Deeper</button>
    <button class="btn btn-hold" onclick="act('{cid}','hold')">&#9208; Hold</button>
    <button class="btn btn-rd" onclick="act('{cid}','redirect')">&#8597; Redirect</button>
  </div>
</div>"""


def build_page(d, sd):
    cards = d.get("cards", [])
    cols = d.get("columns") or sorted({c.get("column", "Ideas") for c in cards})
    by_col = {name: [c for c in cards if c.get("column", cols[0]) == name] for name in cols}
    funnel = "".join(
        f'<div class="fstat"><span class="fn">{esc(f["value"])}</span><span class="fl">{esc(f["label"])}</span></div>'
        for f in d.get("funnel", []))
    columns_html = "".join(
        f'<div class="col"><div class="colh">{esc(name)}<span class="cc">{len(by_col[name])}</span></div>'
        + ("".join(card_html(c) for c in by_col[name]) or '<div class="empty">-</div>')
        + "</div>" for name in cols)
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{esc(d.get('title','Venture Board'))}</title>
<style>
:root{{--bg:#fff;--fg:#1a1a1a;--card:#f8f9fa;--bd:#dee2e6;--chip:#e9ecef;--chipf:#495057;--acc:#228be6;--mut:#868e96;--pan:#f1f3f5;--go:#2f9e44;--goif:#f08c00;--kill:#e03131;--park:#868e96;}}
@media(prefers-color-scheme:dark){{:root{{--bg:#1a1b1e;--fg:#c1c2c5;--card:#25262b;--bd:#373a40;--chip:#2c2e33;--chipf:#909296;--acc:#4dabf7;--mut:#5c5f66;--pan:#25262b;--go:#51cf66;--goif:#ffa94d;--kill:#ff6b6b;--park:#909296;}}}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:system-ui,-apple-system,sans-serif;background:var(--bg);color:var(--fg);padding:1rem;max-width:78rem;margin:0 auto}}
.banner{{background:var(--pan);border:1px solid var(--bd);border-radius:.5rem;padding:.5rem 1rem;margin-bottom:.75rem;font-size:.78rem;color:var(--mut);word-break:break-all}}
h1{{font-size:1.4rem;margin-bottom:.1rem}} .sub{{color:var(--mut);font-size:.92rem;margin-bottom:1rem}}
.funnel{{display:flex;gap:.75rem;flex-wrap:wrap;margin-bottom:1rem}}
.fstat{{background:var(--pan);border:1px solid var(--bd);border-radius:.6rem;padding:.6rem 1rem;min-width:6rem;text-align:center}}
.fn{{display:block;font-size:1.8rem;font-weight:800;line-height:1}} .fl{{font-size:.72rem;color:var(--mut);text-transform:uppercase;letter-spacing:.03em}}
.legend{{background:var(--pan);border:1px solid var(--bd);border-radius:.5rem;padding:.7rem 1rem;margin-bottom:1rem;font-size:.8rem;line-height:1.7}}
.legend b{{font-size:.75rem;text-transform:uppercase;color:var(--mut)}} .legend .r{{display:flex;flex-wrap:wrap;gap:.4rem .9rem;align-items:center;margin-top:.3rem}}
.strip{{display:flex;align-items:center;gap:.5rem;font-size:.78rem;margin-bottom:.75rem;color:var(--mut)}}
.dot{{width:.5rem;height:.5rem;border-radius:50%;background:var(--mut);display:inline-block}} .dot-processing{{background:var(--acc);animation:p 1.2s infinite}} @keyframes p{{0%,100%{{opacity:1}}50%{{opacity:.4}}}}
.board{{display:flex;gap:.9rem;overflow-x:auto;padding-bottom:.75rem}}
.col{{flex:0 0 17rem;min-width:17rem}}
.colh{{font-size:.8rem;font-weight:700;text-transform:uppercase;letter-spacing:.03em;color:var(--mut);padding:.3rem .1rem;display:flex;align-items:center;gap:.4rem;border-bottom:2px solid var(--bd);margin-bottom:.6rem}}
.cc{{background:var(--chip);color:var(--chipf);border-radius:1rem;font-size:.72rem;padding:0 .45rem;font-weight:700}}
.empty{{color:var(--mut);font-size:.8rem;padding:.5rem .1rem}}
.card{{background:var(--card);border:1px solid var(--bd);border-radius:.5rem;padding:.7rem;margin-bottom:.7rem;transition:opacity .2s}} .card.acted{{opacity:.5}}
.chd{{display:flex;align-items:center;gap:.4rem;margin-bottom:.4rem;flex-wrap:wrap}}
.ctitle{{font-size:.92rem;font-weight:600;line-height:1.25}}
.pill{{font-size:.66rem;font-weight:700;padding:.15rem .45rem;border-radius:1rem;color:#fff;white-space:nowrap}}
.pill-go{{background:var(--go)}}.pill-goif{{background:var(--goif)}}.pill-kill{{background:var(--kill)}}.pill-park{{background:var(--park)}}.pill-none{{background:var(--chip);color:var(--chipf)}}
.chips{{display:flex;gap:.3rem;flex-wrap:wrap;margin-bottom:.4rem}}
.chip{{font-size:.68rem;padding:.1rem .4rem;border-radius:1rem;background:var(--chip);color:var(--chipf)}}
.chip-fit-high{{background:var(--go);color:#fff}}.chip-fit-cond{{background:var(--goif);color:#fff}}.chip-fit-low{{background:var(--chip);color:var(--chipf)}}
.csum{{font-size:.8rem;line-height:1.45;margin-bottom:.35rem}} .take{{font-size:.74rem;color:var(--acc);font-weight:600;margin-bottom:.45rem}}
.note{{width:100%;border:1px solid var(--bd);border-radius:.35rem;padding:.35rem;font-size:.78rem;background:var(--bg);color:var(--fg);resize:vertical;margin-bottom:.45rem}}
.acts{{display:flex;gap:.3rem;flex-wrap:wrap}}
.btn{{border:none;padding:.32rem .55rem;border-radius:.35rem;font-size:.74rem;font-weight:600;cursor:pointer}} .btn:hover{{filter:brightness(1.1)}} .btn:disabled{{opacity:.4;cursor:default}}
.btn-ok{{background:var(--go);color:#fff}}.btn-hold{{background:var(--chip);color:var(--chipf)}}.btn-rd{{background:var(--goif);color:#fff}}
.general{{margin:1.25rem 0 .5rem}} .general label{{display:block;font-size:.8rem;color:var(--mut);margin-bottom:.3rem}}
.general textarea{{width:100%;border:1px solid var(--bd);border-radius:.375rem;padding:.55rem;font-size:.9rem;background:var(--card);color:var(--fg);resize:vertical}}
.sendbar{{position:sticky;bottom:0;background:var(--bg);border-top:1px solid var(--bd);padding:.7rem 0;display:flex;align-items:center;gap:1rem}}
#send{{background:var(--acc);color:#fff;border:none;padding:.5rem 1.2rem;border-radius:.375rem;font-size:.9rem;font-weight:600;cursor:pointer}} #send:disabled{{opacity:.5}}
.count,#status{{font-size:.83rem;color:var(--mut)}}
.res{{margin-top:.4rem;padding:.35rem .6rem;border-radius:.35rem;font-size:.78rem;font-weight:600;background:var(--acc);color:#fff}}
</style></head><body>
<div class="banner"><b>Session:</b> {esc(sd)}</div>
<h1>{esc(d.get('title','Venture Board'))}</h1><div class="sub">{esc(d.get('subtitle',''))}</div>
<div class="funnel">{funnel}</div>
<div class="strip"><span class="dot" id="dot"></span><span id="slabel">idle</span></div>
<div class="legend"><b>Legend</b>
  <div class="r"><span class="pill pill-go">GO</span>clear yes<span class="pill pill-goif">GO-IF</span>yes, pending one test<span class="pill pill-kill">KILL</span>adversarially killed<span class="pill pill-park">PARK</span>real but not your fit/now</div>
  <div class="r" style="margin-top:.4rem">&#128077;<b>Deeper</b>=run the next loop &#9208;<b>Hold</b>=park &#8597;<b>Redirect</b>=your note steers it &nbsp;·&nbsp; fit=match to YOUR assets. Columns=pipeline stage.</div>
</div>
<div class="board">{columns_html}</div>
<div class="general"><label>General comments (whole board):</label><textarea id="gc" rows="2" placeholder="session-wide input - rides the submit"></textarea></div>
<div class="sendbar"><button id="send" onclick="sendAll()">Send to session</button><span class="count" id="qc">0 queued</span><span id="status"></span></div>
<script>
var queue={{}};
function act(id,a){{var t=document.getElementById('note-'+id);queue[id]={{target:String(id),action:a,raw_words:(t&&t.value.trim())||null,at:new Date().toISOString()}};var c=document.getElementById('card-'+id);c.classList.add('acted');var b=c.querySelectorAll('.btn');for(var i=0;i<b.length;i++)b[i].disabled=true;document.getElementById('qc').textContent=Object.keys(queue).length+' queued';}}
async function sendAll(){{document.getElementById('send').disabled=true;var k=Object.keys(queue),sent=0,err=0;for(var i=0;i<k.length;i++){{try{{var r=await fetch('/annotate',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify(queue[k[i]])}});r.ok?sent++:err++;}}catch(e){{err++;}}}}var g=document.getElementById('gc').value.trim();try{{await fetch('/annotate',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{target:'__session__',action:'submit',raw_words:g||null,at:new Date().toISOString()}})}});sent++;}}catch(e){{err++;}}queue={{}};document.getElementById('qc').textContent='0 queued';document.getElementById('status').textContent=sent+' sent'+(err?', '+err+' failed':'');}}
async function poll(){{var d;try{{d=await (await fetch('/status')).json();}}catch(e){{d={{status:'idle'}};}}var s=(d&&d.status)||'idle';document.getElementById('dot').className='dot dot-'+s;document.getElementById('slabel').textContent=s;var rs=(d&&d.results)||[];for(var i=0;i<rs.length;i++){{var t=rs[i].target,c=document.getElementById('card-'+t);if(c&&!document.getElementById('res-'+t)){{var e=document.createElement('div');e.id='res-'+t;e.className='res';e.textContent='-> '+(rs[i].outcome||'done');c.appendChild(e);c.classList.add('acted');}}}}}}
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
