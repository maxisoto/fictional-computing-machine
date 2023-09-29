from ..database import DatabaseConnection
from .exceptions import CustomException


class Canales:
    """Canales model class"""
    def __init__(self, **kwargs):
        self.id_canal = kwargs.get('id_canal')
        self.nombre = kwargs.get('nombre')
        self.descripcion = kwargs.get('descripcion')
        self.id_server = kwargs.get('id_server')

    def serialize(self):
        """Serialize object representation"""
        return {
        
                "id_canal": self.id_canal,
                "nombre": self.nombre,
                "descipcion": self.descripcion,
                "id_server": self.id_server
            
        }    
    @classmethod
    def get_channels(cls):
        query = """SELECT canales.id_canal, canales.nombre, canales.descripcion, servidor.id_server, user_server.id_user 
        FROM ((grupo11.canales 
        INNER JOIN grupo11.servidor ON canales.id_server = servidor.id_server)
        INNER JOIN grupo11.user_server ON servidor.id_server = user_server.id_server)"""
        
        results = DatabaseConnection.fetch_all(query)
        canales = []
        if result is not None:
            for result in results:
                canales.append(Canales(
                    id_canal = result[0],
                    nombre = result[1],
                    descripcion = result[2],
                    id_server = result[3]               
            ))  
            return canales
        else:
            #raise ServerNotFound(404,"Server Not Found",f"NO usuario con id {id_user} NO pertenece a ningun servidor!!!")    
            return {'message': f'El servidor no tiene ningun canal activo. Desea crear uno!'}, 
    
    @classmethod
    def get_channel(cls,id_server):
        query = """SELECT canales.id_canal, canales.nombre, canales.descripcion, servidor.id_server, user_server.id_user 
        FROM ((grupo11.canales 
        INNER JOIN grupo11.servidor ON canales.id_server = servidor.id_server)
        INNER JOIN grupo11.user_server ON servidor.id_server = user_server.id_server)
        WHERE servidor.id_server = %s"""
        params = id_server,
        results = DatabaseConnection.fetch_all(query, params=params)
        canales = []
        if result is not None:
            for result in results:
                canales.append(Canales(
                    id_canal = result[0],
                    nombre = result[1],
                    descripcion = result[2],
                    id_server = result[3]               
            ))  
            return canales
        else:
            #raise ServerNotFound(404,"Server Not Found",f"NO usuario con id {id_user} NO pertenece a ningun servidor!!!")    
            return {'message': f'El servidor no tiene ningun canal activo. Desea crear uno!'}, 400
    
    @classmethod
    def update_channel(cls, canal):
        """Modificar Canal"""

        allowed_columns = {'nombre', 'descripcion', 'id_server'}
        query_parts = []
        params = []
        for key, value in canal.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(canal.id_canal)
        query = "UPDATE grupo11.canales SET " + ", ".join(query_parts) + " WHERE id_canal = %s"
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def create_channel(cls, canal):
        """Crear Usuario"""

        query = """INSERT INTO grupo11.canales (nombre, descripcion, id_server) 
        VALUES (%s, %s, %s)"""

        params = canal.nombre, canal.descripcion, canal.id_server, 
        cursor = DatabaseConnection.execute_query(query, params=params)

        if cursor.rowcount == 1:
            id_canal = cursor.lastrowid
            return id_canal
        
        else:
            return {'message': f'Error no se pudo crear el nuevo canal'}, 400
        
    @classmethod
    def get(cls, canal = None):
        if canal and canal.id_canal:
            query = """SELECT canales.id_canal, canales.nombre, canales.descripcion, canales.id_server
            FROM ((grupo11.canales 
            INNER JOIN grupo11.servidor ON canales.id_server = servidor.id_server)
            INNER JOIN grupo11.user_server ON servidor.id_server = user_server.id_server)
            WHERE canales.id_canal = %s"""
            params = (canal.id_canal,)
            result = DatabaseConnection.fetch_one(query, params)
            return cls(**dict(zip(cls._keys, result))) if result else None
        elif canal and canal.id_server:
            query = """SELECT canales.id_canal, canales.nombre, canales.descripcion, canales.id_server
            FROM ((grupo11.canales 
            INNER JOIN grupo11.servidor ON canales.id_server = servidor.id_server)
            INNER JOIN grupo11.user_server ON servidor.id_server = user_server.id_server)
            WHERE canal.id_server = %s"""
            params = (canal.id_server,)
            results = DatabaseConnection.fetch_all(query, params)
            return [cls(**dict(zip(cls._keys, row))) for row in results]
        else:
            query = """SELECT canales.id_canal, canales.nombre, canales.descripcion, servidor.id_server, user_server.id_user 
            FROM ((grupo11.canales 
            INNER JOIN grupo11.servidor ON canales.id_server = servidor.id_server)
            INNER JOIN grupo11.user_server ON servidor.id_server = user_server.id_server)"""
            results = DatabaseConnection.fetch_all(query)
            return [cls(**dict(zip(cls._keys, row))) for row in results]


    @classmethod
    def delete_channel(cls, server):
        pass

    @classmethod
    def exist(self, id_server):
        pass
