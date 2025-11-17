from flask import Flask, request
import json, os

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask is working!"

@app.route("/receive_usage", methods=["POST"])
def receive_usage():
    data = request.get_json()
    if not data:
        return {"ok": False, "error": "no json"}, 400

    os.makedirs("data", exist_ok=True)
    with open("data/today.json", "w") as f:
        json.dump(data, f, indent=2)

    return {"ok": True, "saved": "data/today.json"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

