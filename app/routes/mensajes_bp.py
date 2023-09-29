from flask import Blueprint

from ..controllers.mensajes_controller import MensajeController

mensajes_bp = Blueprint('mensajes_bp', __name__)

mensajes_bp.route('/<int:id_canal>', methods=['GET'])(MensajeController.cargar_msj)
mensajes_bp.route('/', methods=['POST'])(MensajeController.nuevo_msj)
