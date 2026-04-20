import os
os.environ['PGCLIENTENCODING'] = 'utf-8'
from flask import Flask, jsonify
from flask_cors import CORS
from routes.user_routes import user_bp
from routes.ticket_routes import ticket_bp

app = Flask(__name__)
# CORS é obrigatório pois o Frontend (Bun) roda em porta diferente do Backend (Flask)
CORS(app) 

# Registra as rotas
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(ticket_bp, url_prefix='/api')

# Rota de teste simples (Passo 2)
@app.route('/api/test', methods=['GET'])
def test_api():
    return jsonify({"mensagem": "Backend rodando com sucesso!", "status": "OK"}), 200

if __name__ == '__main__':
    # Roda na porta 5000
    app.run(debug=True, port=5000)