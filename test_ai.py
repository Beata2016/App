from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # aby frontend mógł wysyłać żądania

MAX_QUERIES = 50
query_count = 0

@app.route("/api/chat", methods=["POST"])
def chat():
    global query_count
    if query_count >= MAX_QUERIES:
        return jsonify({"reply": "⚠️ Osiągnięto dzienny limit zapytań"})
    
    data = request.json
    msg = data.get("message", "")
    lang = data.get("lang", "pl")
    
    # tutaj możesz dodać własną logikę AI
    reply = f"Odpowiedź ({lang}): {msg[::-1]}"  # np. odwrócona wiadomość, jako przykład
    
    query_count += 1
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
