# -*- coding: utf-8 -*-

from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from app.routes.numbers_routes import numbers_bp  # Corrigido nome do arquivo

def create_app():
    """Cria e configura a aplicação Flask."""
    app = Flask(__name__)

    app.register_blueprint(numbers_bp)

    SWAGGER_URL = "/swagger"
    API_URL = "/static/swagger.yaml"
    
    swagger_ui = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
    app.register_blueprint(swagger_ui, url_prefix=SWAGGER_URL)

    return app


app = create_app()