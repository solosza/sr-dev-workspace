"""render_server.py — Annotation collection server for the render skill.

Usage: python render_server.py <session_dir>

Serves <session_dir>/page.html at GET / and collects annotations at POST /annotate.
Serves <session_dir>/session-reply.json at GET /status (or {"status":"idle"} when absent).
Binds 127.0.0.1 on an ephemeral port; prints PORT=<n> to stdout (flushed) on startup.

SINGLE-OUTPUT-PATH LAW (RRT-02): The ONLY filesystem writes in this entire file are
<session_dir>/.annotations.tmp (tempfile) and os.replace to <session_dir>/annotations.json.
Served reads: page.html (GET /), session-reply.json (GET /status).
No logs-to-file, no state files, nothing else.
"""

import http.server
import json
import os
import socketserver
import sys

REQUIRED_FIELDS = ("target", "action", "raw_words", "at")


class RenderHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/status":
            reply_path = os.path.join(self.server.session_dir, "session-reply.json")
            if os.path.isfile(reply_path):
                with open(reply_path, "rb") as f:
                    content = f.read()
            else:
                content = b'{"status": "idle"}'
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return
        if self.path != "/":
            self.send_error(404)
            return
        page_path = os.path.join(self.server.session_dir, "page.html")
        if not os.path.isfile(page_path):
            self.send_error(404, "page.html not found in session dir")
            return
        with open(page_path, "rb") as f:
            content = f.read()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(content)

    def do_POST(self):
        if self.path != "/annotate":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", 0))
        if length == 0:
            self.send_error(400, "Empty body")
            return
        raw = self.rfile.read(length)
        try:
            annotation = json.loads(raw)
        except json.JSONDecodeError:
            self.send_error(400, "Malformed JSON")
            return
        if not isinstance(annotation, dict):
            self.send_error(400, "Body must be a JSON object")
            return
        missing = [f for f in REQUIRED_FIELDS if f not in annotation]
        if missing:
            self.send_error(400, "Missing fields: " + ", ".join(missing))
            return

        annotations_path = os.path.join(self.server.session_dir, "annotations.json")
        tmp_path = os.path.join(self.server.session_dir, ".annotations.tmp")

        if os.path.isfile(annotations_path):
            with open(annotations_path, "r", encoding="utf-8") as f:
                existing = json.loads(f.read())
        else:
            existing = []

        existing.append(annotation)

        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(existing, f, indent=2, ensure_ascii=False)
        os.replace(tmp_path, annotations_path)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps({"ok": True}).encode())

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def log_message(self, format, *args):
        pass


def main():
    if len(sys.argv) != 2:
        print("Usage: python render_server.py <session_dir>", file=sys.stderr)
        sys.exit(1)

    session_dir = os.path.abspath(sys.argv[1])
    if not os.path.isdir(session_dir):
        print(f"Error: {session_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    server = socketserver.TCPServer(("127.0.0.1", 0), RenderHandler)
    server.session_dir = session_dir
    port = server.server_address[1]
    print(f"PORT={port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
