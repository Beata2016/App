from flask import Flask, request, jsonify, session, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
app.secret_key = 'sekretnyklucz123'  # potrzebny do sesji
CORS(app)

MAX_QUERIES = 50
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Serwowanie pliku HTML
@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'ai-chat.html')  # <- zmieniono podkreślnik na myślnik

# Endpoint czatu
@app.route('/api/chat', methods=['POST'])
def chat():
    if 'count' not in session:
        session['count'] = 0
    if session['count'] >= MAX_QUERIES:
        return jsonify({'reply': '⚠️ Osiągnięto dzienny limit zapytań'})
    
    data = request.json
    message = data.get('message', '')
    session['count'] += 1
    
    # Prosta darmowa odpowiedź (echo)
    reply = f"🤖 Echo AI: {message}"
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

