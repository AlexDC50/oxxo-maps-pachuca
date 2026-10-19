from flask import Flask
from flask_cors import CORS
from routes.sucursales import sucursales_bp

app = Flask(__name__)
CORS(app) # Vital para que tu HTML y Android puedan consumir la API sin bloqueos[cite: 5]

app.register_blueprint(sucursales_bp)

if __name__ == '__main__':
    # use_reloader=False evita el error [WinError 10038] en Windows
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)