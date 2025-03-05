# -*- coding: utf-8 -*-

from flask import Flask
from app.routes.numbers import numbers_bp
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Registra o blueprint
app.register_blueprint(numbers_bp)

# Configuração do Swagger UI (opcional)
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.yaml"

swagger_ui = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swagger_ui, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)