from ..models.servidor_model import Servidor
from flask import request
from ..models.exceptions import ServerNotFound,InvalidDataError

class ServidorController:
    
    @classmethod
    def listar_servidores(cls):
        """Listar todos los servidores activos"""
        server_objects = Servidor.get_servers_activos()
        servidores = []
        for server in server_objects:
            servidores.append(server.serialize())
        return servidores, 200
    
    @classmethod
    def buscar_servidor_nombre(cls,nombre):
        """Metodo para buscar un servidor por un nombre"""
        result = Servidor.buscar_serv_nombre(nombre)
        if result is not None:
            return result.serialize(), 200

    @classmethod
    def listar_servidor_usuario(cls,id_user):
        """Metodo para listar los servidores activos a los que pertenece un usuario"""
        server_objects = Servidor.get_server_user(id_user)
        servidores = []
        for server in server_objects:
            servidores.append(server.serialize())
        return servidores, 200

    @classmethod
    def crear_servidor(cls,id_user):
        """Metodo para que un usuario pueda crear un servidor"""
        data = request.json

        if 'nombre' not in data:
            raise InvalidDataError(400,'Invalid Data Error','El nombre del Servidor es obligatorio, Debe ingresarlo !!!')
        
        nuevo_servidor = Servidor(
            nombre = data.get('nombre'),
            descripcion = data.get('descripcion'),
            f_creacion = data.get('f_creacion'),
            activo = data.get('activo'),
            icono = data. get('icono')
        )
        nomb_server = data.get('nombre')
        Servidor.create_server(nuevo_servidor,id_user)
        return {'message': f'Se creo correctamente al servidor = {nomb_server}'}, 200


    @classmethod
    def update_servidor(cls, id_server,id_user):
        """Metodo para modificar un servidor siempre y cuando el usuario sea propietario"""
        data = request.json

        servidor = Servidor(
            id_server = id_server,
            nombre = data.get('nombre'),
            descripcion = data.get('servidor'),
            f_creacion = data.get('f_creacion'),
            activo = data.get('activo'),
            icono = data. get('icono')
        )

        # Primeramente verficamos si el usuario es propietario
        es_propietario = Servidor.user_es_propietario(id_user,id_server)
        if es_propietario == True:
            Servidor.update_server(servidor)
            return {'message': f'Se actualizo correctamente el Servidor = {id_server}'}, 200
        else:
            raise ServerNotFound(404, "Server Not Found",f'El usuario no es propietario del Servidor id {id_server}, por lo tanto no lo puede modificar')


    @classmethod
    def delete_servidor(cls, id_server):
        pass
