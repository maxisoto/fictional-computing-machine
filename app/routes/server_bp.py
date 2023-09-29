from flask import Blueprint

from ..controllers.servidor_controller import ServidorController

server_bp = Blueprint('server_bp', __name__)

server_bp.route('/', methods=['GET'])(ServidorController.listar_servidores)
server_bp.route('/<string:nombre>', methods=['GET'])(ServidorController.buscar_servidor_nombre)
server_bp.route('/<int:id_user>', methods=['GET'])(ServidorController.listar_servidor_usuario)
server_bp.route('/<int:id_user>', methods=['POST'])(ServidorController.crear_servidor)
server_bp.route('/<int:id_server>,<int:id_user>', methods=['PUT'])(ServidorController.update_servidor)
#server_bp.route('/<int:id_server>', methods=['DELETE'])(ServidorController.delete_server)