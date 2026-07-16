import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # للسماح لأي واجهة بالاتصال بالسيرفر

# قراءة التوكن من متغير البيئة
BOT_TOKEN = os.environ.get("BOT_TOKEN")

@app.route("/", defaults={"path": ""}, methods=["GET", "POST"])
@app.route("/<path:path>", methods=["GET", "POST"])
def index(path):
    return jsonify({
        "message": "Bot API is running",
        "token_configured": bool(BOT_TOKEN)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
