from flask import Flask, render_template, request, jsonify
from weather import get_weather

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data["message"]

    # Get weather info
    reply = get_weather(user_message)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
