from ..models.canales_model import Canales
from flask import request
from ..models.exceptions import ServerNotFound,InvalidDataError

class CanalController:
    @classmethod
    def buscar_canales_servidor(cls, id_server):
        """Metodo para listar los canales activos de un servidor"""
        canal_objects = Canales.get_channel(id_server)
        canales = []
        for channel in canal_objects:
            canales.append(channel.serialize())
        return canales, 200
       
    @classmethod
    def crear_canal(cls):
        """Crear nuevo canal"""
        data = request.json
        if 'nombre' not in data:
            #raise InvalidDataError(400,'Invalid Data Error','El nombre del Canal es obligatorio, Debe ingresarlo !!!')
            return {'message': f'El nombre del Canal es obligatorio, Debe ingresarlo !!!'}, 400
        nuevo_canal = Canales(
            nombre = data.get('nombre'),
            descripcion = data.get('descripcion'),
            id_server = data.get('id_server')
        )
        nomb_canal = data.get('nombre')
        return_canal = Canales.create_channel(nuevo_canal)
        return {'message': f'Se creo correctamente el Canal = {return_canal}'}, 200

    @classmethod
    def update_canal(cls, id_canal,id_user):
        pass

    @classmethod
    def delete_canal(cls, id_canal):
        pass
