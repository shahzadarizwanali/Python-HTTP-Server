from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse
import csv
import os

HOST = "127.0.0.1"
PORT = 5000

CSV_FILE = "companies_data.csv"


def list_companies():
    companies = []

    if os.path.isfile(CSV_FILE):
        with open(CSV_FILE, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                companies.append(row)
    return companies


def add_company(data):
    fieldnames = ["name", "owner", "address", "zip", "country"]
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()

        writer.writerow(data)
    return {"message": "Company added!"}


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

    def do_POST(self):
        if self.path == "/add-company":
            content_length = int(self.headers["Content-Length"])
            POST_data = self.rfile.read(content_length)
            company_data = json.loads(POST_data.decode("utf-8"))
            result = add_company(company_data)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())


if __name__ == "__main__":
    print(f"Company Server Start at http://{HOST}:{PORT}")
    server = HTTPServer((HOST, PORT), CompanyRequestHandler)
    server.serve_forever()
