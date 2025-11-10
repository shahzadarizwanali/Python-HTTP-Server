from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from company_data import list_companies
from urllib.parse import urlparse

HOST = "127.0.0.1"
PORT = 5000


class CompanyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)

        if parsed_path.path == "/companies":
            companies = list_companies()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"companies": companies}).encode())

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")


if __name__ == "__main__":
    print(f"Company Server Start at http://{HOST}:{PORT}")
    server = HTTPServer((HOST, PORT), CompanyRequestHandler)
    server.serve_forever()
