from http.server import SimpleHTTPRequestHandler
import socketserver
import os

PORT = int(os.environ.get("PORT", 8000))

Handler = SimpleHTTPRequestHandler

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b""]

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()

