"""Minimal HTTP server for click-fault probe. Serves two pages for navigation testing."""
import http.server, os

os.chdir("D:/my_ai_projects/project_test_repos/sr_dev_workspace/scratchpad")

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/page_a.html":
            self.path = "/bare_click_page.html"
        elif self.path == "/page_b.html":
            self.path = "/bare_click_page_b.html"
        return super().do_GET()

    def log_message(self, format, *args):
        pass  # suppress request logs

if __name__ == "__main__":
    with http.server.HTTPServer(("127.0.0.1", 8019), Handler) as s:
        print("Serving on 8019")
        s.serve_forever()
