#!/usr/bin/python3
"""Simple API server using Python's http.server module."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handle GET requests for a basic API."""

    def _send_json(self, status_code, payload):
        """Send a JSON response."""
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_text(self, status_code, message):
        """Send a plain text response."""
        body = message.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        """Route GET endpoints and return appropriate responses."""
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            self._send_json(200, {"name": "John", "age": 30, "city": "New York"})
        elif self.path == "/status":
            self._send_text(200, "OK")
        elif self.path == "/info":
            self._send_json(
                200,
                {
                    "version": "1.0",
                    "description": "A simple API built with http.server",
                },
            )
        else:
            self._send_text(404, "Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Start the HTTP server."""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
