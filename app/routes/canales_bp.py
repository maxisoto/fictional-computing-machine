from flask import Blueprint

from ..controllers.canales_controller import CanalController

canales_bp = Blueprint('canales_bp', __name__)

# canales_bp.route('/', methods=['GET'])(CanalController.get_all)
# canales_bp.route('/<int:id_canal>', methods=['GET'])(CanalController.get)
# canales_bp.route('/', methods=['POST'])(CanalController.create)
# canales_bp.route('/<int:id_canal>', methods=['PUT'])(CanalController.update)
# canales_bp.route('/<int:id_canal>', methods=['DELETE'])(CanalController.delete)