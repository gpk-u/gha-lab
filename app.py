from http.server import BaseHTTPRequestHandler, HTTPServer


def health() -> dict:
    return {"status": "ok"}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200 if self.path == "/health" else 404)
        self.end_headers()
        if self.path == "/health":
            self.wfile.write(b'{"status":"ok"}')


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
