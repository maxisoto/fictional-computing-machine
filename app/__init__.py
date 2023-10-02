
from flask import Flask
from flask_cors import CORS
from config import Config

from .routes.usuario_bp import usuario_bp
from .routes.server_bp import server_bp
from .routes.mensajes_bp import mensajes_bp
from .routes.canales_bp import canales_bp
from .routes.error_handlers import errors

from .database import DatabaseConnection

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    CORS(app, supports_credentials=True)

    app.config.from_object(
        Config
    )

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(usuario_bp, url_prefix = '/users')
    app.register_blueprint(server_bp, url_prefix = '/servers')
    app.register_blueprint(mensajes_bp, url_prefix = '/messages')
    app.register_blueprint(canales_bp, url_prefix = '/channels')
    app.register_blueprint(errors, url_prefix = '/errors')

    return app