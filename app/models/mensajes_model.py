from ..database import DatabaseConnection
from .exceptions import CustomException


class Mensaje:
    """Mensaje model class"""
    def __init__(self, **kwargs):
        self.id_mensaje = kwargs.get('id_mensaje')
        self.cuerpo = kwargs.get('cuerpo')
        self.f_envio = kwargs.get('f_envio')
        self.id_user = kwargs.get('id_user')
        self.id_canal = kwargs.get('id_canal')
        self.visible = kwargs.get('visible')

    def serialize(self):
        """Serialize object representation"""
        return {
                "id_mensaje": self.id_mensaje,
                "cuerpo": self.cuerpo,
                "f_envio": self.f_envio,
                "id_user": self.id_user,
                "id_canal": self.id_canal,
                "visible": self.visible        
        }

    @classmethod
    def get_msj(cls,id_canal):
        query = """SELECT * FROM grupo11.mensajes
        WHERE id_canal = %s
        ORDER BY id_mensaje DESC LIMIT 20"""
        params = id_canal,
        results = DatabaseConnection.fetch_all(query, params=params)
        mensajes = []
        if result is not None:
            for result in results:
                mensajes.append(Mensaje(
                    id_mensaje = result[0],
                    cuerpo = result[1],
                    f_envio = result[2],
                    id_user = result[3],
                    id_canal = result[4],
                    visible = result[5]            
            ))  
            return mensajes
        else:
            #raise ServerNotFound(404,"Server Not Found",f"NO usuario con id {id_user} NO pertenece a ningun servidor!!!")    
            return {'message': f'Sin mensajes. Desea crear uno!'}, 400
    
    @classmethod
    def update_msj(cls, server):
        pass

    @classmethod
    def create_msj(cls, mensaje):
        """Crear Mensaje"""
        query = """INSERT INTO grupo11.mensajes (cuerpo, id_user, id_canal) 
        VALUES (%s, %s, %s)"""

        params = mensaje.cuerpo, mensaje.id_user, mensaje.id_canal, 
        cursor = DatabaseConnection.execute_query(query, params=params)

        if cursor.rowcount == 1:
            id_mensaje = cursor.lastrowid
            return id_mensaje
        
        else:
            return {'message': f'Error, NO se pudo crear el nuevo mensaje'}, 400

    @classmethod
    def delete_msj(cls, mensaje):
        pass

    @classmethod
    def buscar_msj(self, mensaje):
        pass
