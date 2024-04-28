from flask import Flask
from .error_handler import register_error_handlers

def create_app():
    app = Flask(__name__)
    from .routes import api
    app.register_blueprint(api)
    register_error_handlers(app)  # Registra os handlers de erro
    return app
