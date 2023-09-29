from flask import Blueprint

from ..controllers.usuario_controller import UsuarioController

usuario_bp = Blueprint('usuario_bp', __name__)

usuario_bp.route('/bienvenida', methods=['GET', 'POST'])(UsuarioController.bienvenida)
usuario_bp.route('/login', methods=['POST'])(UsuarioController.login)
#usuario_bp.route('/profile', methods=['GET'])(UsuarioController.show_profile)
usuario_bp.route('/logout', methods=['GET'])(UsuarioController.logout)
usuario_bp.route('/', methods=['GET'])(UsuarioController.listar_usuarios)
usuario_bp.route('/<int:id_user>', methods=['GET'])(UsuarioController.buscar_usuario)
usuario_bp.route('/', methods=['POST'])(UsuarioController.crear_usuario)
usuario_bp.route('/<int:id_user>', methods=['PUT'])(UsuarioController.update_usuario)
usuario_bp.route('/<int:id_user>', methods=['DELETE'])(UsuarioController.delete_usuario)
usuario_bp.route('/verificar', methods=['POST'])(UsuarioController.verificar_respuesta)
usuario_bp.route('/profile', methods=['GET'])(UsuarioController.show_profile)
usuario_bp.route('/actualizar_pass', methods=['PUT'])(UsuarioController.update_usuario)
