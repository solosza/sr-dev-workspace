"""generate.py — Review-board page generator.

Usage: python generate.py <items_json_path> <session_dir>
Writes <session_dir>/page.html — a self-contained review board.
"""

import html
import json
import os
import sys


def build_card(item):
    n = html.escape(str(item["number"]))
    title = html.escape(str(item["title"]))
    scope = html.escape(str(item.get("scope", "")))
    priority = html.escape(str(item.get("priority", "normal")))
    summary = html.escape(str(item.get("summary", "")))
    return f"""<div class="card" data-number="{n}" id="card-{n}">
  <div class="card-header">
    <span class="card-number">#{n}</span>
    <h3 class="card-title">{title}</h3>
  </div>
  <div class="chips">
    <span class="chip chip-scope">{scope}</span>
    <span class="chip chip-priority chip-priority-{priority}">{priority}</span>
  </div>
  <p class="card-summary">{summary}</p>
  <div class="notes-row" id="notes-row-{n}" style="display:none">
    <label for="notes-{n}">Notes:</label>
    <textarea id="notes-{n}" rows="2" placeholder="Your words (verbatim into kernel)"></textarea>
  </div>
  <div class="actions">
    <button class="btn btn-accept" onclick="act('{n}','accept')">Accept</button>
    <button class="btn btn-iterate" onclick="act('{n}','iterate')">Iterate</button>
    <button class="btn btn-reject" onclick="act('{n}','reject')">Reject</button>
    <button class="btn btn-skip" onclick="act('{n}','skip')">Skip</button>
    <button class="btn btn-defer" onclick="act('{n}','defer')">Defer</button>
  </div>
</div>"""


def build_page(items, session_dir):
    cards_html = "\n".join(build_card(item) for item in items)
    session_dir_escaped = html.escape(session_dir)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Review Board</title>
<style>
:root {{
  --bg: #fff; --fg: #1a1a1a; --card-bg: #f8f9fa; --card-border: #dee2e6;
  --chip-bg: #e9ecef; --chip-fg: #495057; --accent: #228be6; --danger: #e03131;
  --success: #2f9e44; --muted: #868e96; --notes-bg: #fff; --banner-bg: #f1f3f5;
}}
@media (prefers-color-scheme: dark) {{
  :root {{
    --bg: #1a1b1e; --fg: #c1c2c5; --card-bg: #25262b; --card-border: #373a40;
    --chip-bg: #2c2e33; --chip-fg: #909296; --accent: #4dabf7; --danger: #ff6b6b;
    --success: #51cf66; --muted: #5c5f66; --notes-bg: #2c2e33; --banner-bg: #25262b;
  }}
}}
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: system-ui, -apple-system, sans-serif; background: var(--bg); color: var(--fg); padding: 1rem; max-width: 56rem; margin: 0 auto; }}
.banner {{ background: var(--banner-bg); border: 1px solid var(--card-border); border-radius: .5rem; padding: .75rem 1rem; margin-bottom: 1.5rem; font-size: .85rem; color: var(--muted); word-break: break-all; }}
.banner strong {{ color: var(--fg); }}
h1 {{ font-size: 1.5rem; margin-bottom: 1rem; }}
.card {{ background: var(--card-bg); border: 1px solid var(--card-border); border-radius: .5rem; padding: 1rem; margin-bottom: 1rem; transition: opacity .2s; }}
.card.acted {{ opacity: .45; }}
.card-header {{ display: flex; align-items: baseline; gap: .5rem; margin-bottom: .5rem; }}
.card-number {{ font-weight: 700; color: var(--accent); font-size: .9rem; }}
.card-title {{ font-size: 1.05rem; font-weight: 600; }}
.chips {{ display: flex; gap: .4rem; margin-bottom: .5rem; flex-wrap: wrap; }}
.chip {{ font-size: .75rem; padding: .15rem .5rem; border-radius: 1rem; background: var(--chip-bg); color: var(--chip-fg); }}
.chip-priority-high {{ background: var(--danger); color: #fff; }}
.card-summary {{ font-size: .9rem; line-height: 1.5; margin-bottom: .75rem; color: var(--fg); }}
.notes-row {{ margin-bottom: .75rem; }}
.notes-row label {{ display: block; font-size: .8rem; color: var(--muted); margin-bottom: .25rem; }}
.notes-row textarea {{ width: 100%; border: 1px solid var(--card-border); border-radius: .375rem; padding: .5rem; font-size: .85rem; background: var(--notes-bg); color: var(--fg); resize: vertical; }}
.actions {{ display: flex; gap: .4rem; flex-wrap: wrap; }}
.btn {{ border: none; padding: .4rem .85rem; border-radius: .375rem; font-size: .8rem; font-weight: 600; cursor: pointer; transition: filter .15s; }}
.btn:hover {{ filter: brightness(1.1); }}
.btn:disabled {{ opacity: .4; cursor: default; filter: none; }}
.btn-accept {{ background: var(--success); color: #fff; }}
.btn-iterate {{ background: var(--accent); color: #fff; }}
.btn-reject {{ background: var(--danger); color: #fff; }}
.btn-skip {{ background: var(--chip-bg); color: var(--chip-fg); }}
.btn-defer {{ background: var(--chip-bg); color: var(--chip-fg); }}
.send-bar {{ position: sticky; bottom: 0; background: var(--bg); border-top: 1px solid var(--card-border); padding: .75rem 0; display: flex; align-items: center; gap: 1rem; }}
.send-bar .count {{ font-size: .85rem; color: var(--muted); }}
#send-btn {{ background: var(--accent); color: #fff; border: none; padding: .5rem 1.25rem; border-radius: .375rem; font-size: .9rem; font-weight: 600; cursor: pointer; }}
#send-btn:disabled {{ opacity: .5; cursor: default; }}
#status {{ font-size: .85rem; color: var(--muted); }}
.status-strip {{ background: var(--banner-bg); border: 1px solid var(--card-border); border-radius: .375rem; padding: .5rem 1rem; margin-bottom: 1rem; display: flex; align-items: center; gap: .75rem; font-size: .85rem; }}
.status-dot {{ display: inline-block; width: .5rem; height: .5rem; border-radius: 50%; }}
.status-dot-idle {{ background: var(--muted); }}
.status-dot-processing {{ background: var(--accent); animation: pulse 1.2s infinite; }}
.status-dot-closed {{ background: var(--danger); }}
@keyframes pulse {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: .4; }} }}
.status-label {{ font-weight: 600; }}
.status-time {{ color: var(--muted); }}
.dry-run-bar {{ background: var(--banner-bg); border: 2px dashed var(--card-border); border-radius: .375rem; padding: .5rem 1rem; margin-bottom: 1rem; display: flex; align-items: center; gap: .75rem; font-size: .85rem; }}
.dry-run-bar label {{ cursor: pointer; display: flex; align-items: center; gap: .5rem; font-weight: 600; }}
.dry-run-bar .hint {{ color: var(--muted); }}
.confirm-bar {{ background: var(--banner-bg); border: 1px solid var(--accent); border-radius: .375rem; padding: .5rem .75rem; margin: .5rem 0; display: flex; align-items: center; gap: .75rem; font-size: .85rem; flex-wrap: wrap; }}
.confirm-bar .confirm-q {{ flex: 1; min-width: 10rem; }}
.card-result {{ margin-top: .5rem; padding: .5rem .75rem; border-radius: .375rem; font-size: .85rem; font-weight: 600; }}
.card-result-accepted {{ background: var(--success); color: #fff; }}
.card-result-outcome {{ background: var(--accent); color: #fff; }}
.card-result-rejected {{ background: var(--danger); color: #fff; }}
.card-result-dryrun {{ background: var(--chip-bg); color: var(--chip-fg); border: 1px dashed var(--muted); }}
</style>
</head>
<body>

<div class="banner"><strong>Session:</strong> {session_dir_escaped}</div>
<div class="status-strip" id="status-strip">
  <span class="status-dot status-dot-idle" id="status-dot"></span>
  <span class="status-label" id="status-label">idle</span>
  <span class="status-time" id="status-time"></span>
</div>
<h1>Review Board</h1>
<div class="dry-run-bar">
  <label><input type="checkbox" id="dry-run-toggle"> Dry run</label>
  <span class="hint">&mdash; nothing will be routed</span>
</div>

{cards_html}

<div class="send-bar">
  <button id="send-btn" onclick="sendAll()" disabled>Send to session</button>
  <span class="count" id="queue-count">0 queued</span>
  <span id="status"></span>
</div>

<script>
var queue = {{}};

function act(number, action) {{
  var needsNotes = (action === 'iterate' || action === 'reject');
  var notesRow = document.getElementById('notes-row-' + number);
  var textarea = document.getElementById('notes-' + number);

  if (needsNotes && notesRow.style.display === 'none') {{
    notesRow.style.display = 'block';
    textarea.focus();
    return;
  }}

  var rawWords = textarea ? textarea.value.trim() || null : null;

  queue[number] = {{
    target: String(number),
    action: action,
    raw_words: rawWords,
    at: new Date().toISOString()
  }};
  if (document.getElementById('dry-run-toggle').checked) queue[number].test = true;

  var card = document.getElementById('card-' + number);
  card.classList.add('acted');
  var btns = card.querySelectorAll('.btn');
  for (var i = 0; i < btns.length; i++) btns[i].disabled = true;
  if (notesRow) notesRow.style.display = 'none';

  updateCount();
}}

function updateCount() {{
  var n = Object.keys(queue).length;
  document.getElementById('queue-count').textContent = n + ' queued';
  document.getElementById('send-btn').disabled = (n === 0);
}}

async function sendAll() {{
  var btn = document.getElementById('send-btn');
  var status = document.getElementById('status');
  btn.disabled = true;
  var keys = Object.keys(queue);
  var sent = 0;
  var errors = 0;

  for (var i = 0; i < keys.length; i++) {{
    var annotation = queue[keys[i]];
    try {{
      var resp = await fetch('/annotate', {{
        method: 'POST',
        headers: {{ 'Content-Type': 'application/json' }},
        body: JSON.stringify(annotation)
      }});
      if (resp.ok) {{ sent++; }}
      else {{ errors++; }}
    }} catch (e) {{
      errors++;
    }}
  }}

  queue = {{}};
  updateCount();
  var msg = sent + ' sent';
  if (errors > 0) msg += ', ' + errors + ' failed';
  status.textContent = msg;
}}

async function pollStatus() {{
  var data;
  try {{
    var resp = await fetch('/status');
    if (!resp.ok) throw new Error();
    data = await resp.json();
    if (!data || typeof data !== 'object') throw new Error();
  }} catch (e) {{
    data = {{ status: 'idle' }};
  }}
  renderReply(data);
}}

function renderReply(reply) {{
  var dot = document.getElementById('status-dot');
  var lbl = document.getElementById('status-label');
  var timeEl = document.getElementById('status-time');
  var s = reply.status || 'idle';
  dot.className = 'status-dot status-dot-' + s;
  lbl.textContent = s;
  if (reply.at) {{
    try {{ timeEl.textContent = new Date(reply.at).toLocaleTimeString(); }}
    catch(e) {{ timeEl.textContent = ''; }}
  }} else {{ timeEl.textContent = ''; }}

  var results = reply.results || [];
  var resultTargets = {{}};
  for (var i = 0; i < results.length; i++) {{
    resultTargets[results[i].target] = true;
    renderResult(results[i]);
  }}

  var confirms = reply.confirms || [];
  var activeTargets = {{}};
  for (var i = 0; i < confirms.length; i++) {{
    if (!resultTargets[confirms[i].target]) {{
      activeTargets[confirms[i].target] = true;
      renderConfirmBar(confirms[i]);
    }}
  }}
  var allBars = document.querySelectorAll('.confirm-bar');
  for (var i = 0; i < allBars.length; i++) {{
    var t = allBars[i].getAttribute('data-target');
    if (!activeTargets[t]) allBars[i].remove();
  }}

  var acks = reply.dry_run_ack || [];
  for (var i = 0; i < acks.length; i++) {{
    renderDryRunAck(acks[i]);
  }}
}}

function renderConfirmBar(cfm) {{
  var target = cfm.target;
  if (document.getElementById('confirm-' + target)) return;
  var card = document.getElementById('card-' + target);
  if (!card) return;
  var bar = document.createElement('div');
  bar.className = 'confirm-bar';
  bar.id = 'confirm-' + target;
  bar.setAttribute('data-target', target);
  var q = document.createElement('span');
  q.className = 'confirm-q';
  q.textContent = cfm.question || '';
  bar.appendChild(q);
  var yesBtn = document.createElement('button');
  yesBtn.className = 'btn btn-accept';
  yesBtn.textContent = 'Confirm';
  yesBtn.addEventListener('click', function() {{ answerConfirm(target, 'confirm'); }});
  bar.appendChild(yesBtn);
  var noBtn = document.createElement('button');
  noBtn.className = 'btn btn-skip';
  noBtn.textContent = 'Cancel';
  noBtn.addEventListener('click', function() {{ answerConfirm(target, 'cancel'); }});
  bar.appendChild(noBtn);
  var actions = card.querySelector('.actions');
  if (actions) card.insertBefore(bar, actions);
  else card.appendChild(bar);
}}

async function answerConfirm(target, action) {{
  var bar = document.getElementById('confirm-' + target);
  if (bar) {{
    var btns = bar.querySelectorAll('.btn');
    for (var i = 0; i < btns.length; i++) btns[i].disabled = true;
  }}
  try {{
    await fetch('/annotate', {{
      method: 'POST',
      headers: {{ 'Content-Type': 'application/json' }},
      body: JSON.stringify({{ target: target, action: action, raw_words: null, at: new Date().toISOString() }})
    }});
  }} catch (e) {{}}
}}

function renderResult(result) {{
  var target = result.target;
  if (document.getElementById('result-' + target)) return;
  var card = document.getElementById('card-' + target);
  if (!card) return;
  var actions = card.querySelector('.actions');
  if (actions) actions.remove();
  var notesRow = document.getElementById('notes-row-' + target);
  if (notesRow) notesRow.remove();
  var cbar = document.getElementById('confirm-' + target);
  if (cbar) cbar.remove();
  var outcome = result.outcome || '';
  var div = document.createElement('div');
  div.id = 'result-' + target;
  var cls = 'card-result ';
  if (outcome === 'accepted') {{
    cls += 'card-result-accepted';
    div.textContent = '✓ accepted';
  }} else if (outcome.indexOf('rejected') === 0) {{
    cls += 'card-result-rejected';
    div.textContent = '✗ ' + outcome;
  }} else {{
    cls += 'card-result-outcome';
    div.textContent = '→ ' + outcome;
  }}
  div.className = cls;
  card.appendChild(div);
  card.classList.add('acted');
}}

function renderDryRunAck(target) {{
  if (document.getElementById('dryack-' + target)) return;
  var card = document.getElementById('card-' + target);
  if (!card) return;
  var div = document.createElement('div');
  div.id = 'dryack-' + target;
  div.className = 'card-result card-result-dryrun';
  div.textContent = 'acknowledged (dry run — not routed)';
  card.appendChild(div);
  card.classList.add('acted');
}}

pollStatus();
setInterval(pollStatus, 2000);
</script>

</body>
</html>"""


def main():
    if len(sys.argv) != 3:
        print("Usage: python generate.py <items_json_path> <session_dir>",
              file=sys.stderr)
        sys.exit(1)

    items_path = sys.argv[1]
    session_dir = os.path.abspath(sys.argv[2])

    with open(items_path, "r", encoding="utf-8") as f:
        items = json.load(f)

    if not isinstance(items, list):
        print("Error: input JSON must be an array", file=sys.stderr)
        sys.exit(1)

    page = build_page(items, session_dir)
    out_path = os.path.join(session_dir, "page.html")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page)

    print(f"Written: {out_path}")


if __name__ == "__main__":
    main()
