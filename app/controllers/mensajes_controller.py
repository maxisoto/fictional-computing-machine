from ..models.mensajes_model import Mensaje
from flask import request

class MensajeController:
    
    @classmethod
    def cargar_msj(cls, id_canal):
        """Metodo para listar los mensajes activos de un canal"""
        msj_objects = Mensaje.get_msj(id_canal)
        mensajes = []
        for msj in msj_objects:
            mensajes.append(msj.serialize())
        return mensajes, 200

    @classmethod
    def nuevo_msj(cls):
        """Crear nuevo mensaje"""
        data = request.json
        if 'cuerpo' not in data:
            #raise InvalidDataError(400,'Invalid Data Error','El nombre del Canal es obligatorio, Debe ingresarlo !!!')
            return {'message': f'No se puede enviar mensajes vacios !!!'}, 400
        nuevo_mensaje = Mensaje(
            cuerpo = data.get('cuerpo'),
            id_user = data.get('id_user'),
            id_canal = data.get('id_canal')
        )
        return_msj = Mensaje.create_msj(nuevo_mensaje)
        return {'message': f'Se creo correctamente el Canal = {return_msj}'}, 200

    @classmethod
    def update_msj(cls, id_msj):
        pass

    @classmethod
    def delete_msj(cls, id_msj, id_user):
        pass
