# webhook_server.py – Simulated webhook listener to ingest tasks

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        payload = self.rfile.read(content_length)
        task = json.loads(payload.decode("utf-8"))

        try:
            with open("memory_bank.json", "r") as f:
                tasks = json.load(f)
        except:
            tasks = []

        tasks.append(task)
        with open("memory_bank.json", "w") as f:
            json.dump(tasks, f, indent=2)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Task received and stored.")

def run(server_class=HTTPServer, handler_class=WebhookHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"[webhook_server] Listening on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
