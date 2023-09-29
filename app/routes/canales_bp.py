from flask import Blueprint

from ..controllers.canales_controller import CanalController

canales_bp = Blueprint('canales_bp', __name__)

# canales_bp.route('/<int:id_server>', methods=['GET'])(CanalController.buscar_canales_servidor)
#canales_bp.route('/<int:id_server>', methods=['GET'])(CanalController.get_by_id)
canales_bp.route('/', methods=['GET'])(CanalController.get)
canales_bp.route('/', methods=['POST'])(CanalController.crear_canal)
