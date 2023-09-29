from flask import Blueprint

from ..controllers.mensajes_controller import MensajeController

mensajes_bp = Blueprint('mensajes_bp', __name__)

# mensajes_bp.route('/', methods=['GET'])(MensajeController.get_all)
# mensajes_bp.route('/<int:id_mensaje>', methods=['GET'])(MensajeController.get)
# mensajes_bp.route('/', methods=['POST'])(MensajeController.create)
# mensajes_bp.route('/<int:id_mensaje>', methods=['PUT'])(MensajeController.update)
# mensajes_bp.route('/<int:id_mensaje>', methods=['DELETE'])(MensajeController.delete)