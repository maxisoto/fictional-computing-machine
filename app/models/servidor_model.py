from ..database import DatabaseConnection
from .exceptions import ServerNotFound, InvalidDataError
from datetime import datetime

class Servidor:
    """Servidor model class"""
    def __init__(self, **kwargs):
        self.id_server = kwargs.get('id_server')
        self.nombre = kwargs.get('nombre')
        self.descripcion = kwargs.get('descripcion')
        self.f_creacion = kwargs.get('f_creacion')
        self.icono = kwargs.get('icono')
        self.activo = kwargs.get('activo')
        

    def serialize(self):
        """Serialize object representation"""
        return {
                "id_server": self.id_server,
                "nombre": self.nombre,
                "descripcion": self.descripcion,
                "f_creacion": self.f_creacion,
                "icono": self.icono,
                "activo": self.activo          
        }
    @classmethod
    def get_servers_activos(cls):
        query = """SELECT id_server, nombre, descripcion, f_creacion,
        activo, icono 
        FROM grupo11.servidor
        WHERE servidor.activo = 1"""
        
        results = DatabaseConnection.fetch_all(query)
        servidores = []
        if results is not None:
            for result in results: 
                servidores.append(Servidor(
                    id_server = result[0],
                    nombre = result[1],
                    descripcion = result[2],
                    f_creacion = result[3],
                    activo = result[4],
                    icono = result[5]               
            ))  
        return servidores
    
    @classmethod
    def get_server_user(cls,id_user):
        query = """SELECT servidor.id_server, servidor.nombre, servidor.descripcion, servidor.f_creacion, servidor.activo, servidor.icono, user_server.propietario
        FROM (grupo11.user_server
        INNER JOIN grupo11.servidor ON user_server.id_server = servidor.id_server)
        WHERE user_server.id_user = %s and servidor.activo = 1
        ORDER BY servidor.nombre DESC"""
        params = id_user,
        results = DatabaseConnection.fetch_all(query, params=params)
        servidores = []
        if result is not None:
            for result in results:
                servidores.append(Servidor(
                    id_server = result[0],
                    nombre = result[1],
                    descripcion = result[2],
                    f_creacion = result[3],
                    activo = result[4],
                    icono = result[5]               
            ))  
            return servidores
        else:
            raise ServerNotFound(404,"Server Not Found",f"NO usuario con id {id_user} NO pertenece a ningun servidor!!!")    

            

    @classmethod
    def buscar_serv_id(cls,id_server):
        query = """SELECT id_server, nombre, descripcion, f_creacion,
        activo, icono 
        FROM grupo11.servidor WHERE id_server = %s"""
        params = id_server,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return Servidor(
                id_server = result[0],
                nombre = result[1],
                descripcion = result[2],
                f_creacion = result[3],
                activo = result[4]                 
            )  
        else:   
            raise ServerNotFound(404,"Server Not Found",f"NO se encontro el Servidor con el nombre {Servidor.nombre} NO existe, verifique este dato!!!")    
    
    @classmethod
    def update_server(cls, server):
        """Modificar Servidor"""
        allowed_columns = {'nombre', 'descripcion', 'f_creacion',
                           'activo', 'icono'}
        query_parts = []
        params = []
        for key, value in server.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(server.id_user)
        query = "UPDATE grupo11.servidor SET " + ", ".join(query_parts) + " WHERE id_server = %s"
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def create_server(cls, server, id_user):
        """Crear Servidor"""

        query1 = """INSERT INTO grupo11.servidor (nombre, descripcion,
        activo, icono) 
        VALUES (%s, %s, %s, %s)"""

        query2 = """INSERT INTO grupo11.user_server (propietario, id_user, id_server) 
        VALUES (%s, %s, %s)"""

        """Primeramente Creamos el servidor"""
        params1 = server.nombre, server.descripcion, \
                 server.activo, server.icono
        cursor = DatabaseConnection.execute_query(query1, params=params1)

        if cursor.rowcount == 1:
            """Si el servidor nuevo se creo correctamente le asigno el propietario del servidor"""
            id_server = cursor.lastrowid
            params2 = 1, id_user, id_server
            cursor = DatabaseConnection.execute_query(query2, params=params2)
        else:
            raise InvalidDataError(400,'Invalid Data Error','Ingreso datos incorrectos')

    @classmethod
    def asignar_usuario_serv(cls, id_user, id_server):
        """Metodo para asignar unir un usuario a un servidor"""
        query = """INSERT INTO grupo11.user_server (propietario, id_user, id_server) 
        VALUES (%s, %s, %s)"""
        params = 0, id_user, id_server
        cursor = DatabaseConnection.execute_query(query, params=params)

        if cursor.rowcount == 1:
            id_usuario = cursor.lastrowid
            return id_usuario
        
        else:
            raise InvalidDataError(400,'Invalid Data Error','Ingreso datos incorrectos')


    @classmethod
    def user_existe_server(self, id_user, id_server):
        """Metodo para verificar si un usuario existe en un servidor"""
        query = """SELECT * 
        FROM (grupo11.user_server
        INNER JOIN grupo11.usuarios ON user_server.id_user = usuarios.id_user)
        WHERE user_server.id_server = %s and user_server.id_user = %s """
        params = id_server,id_user,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            respuesta = True
            print('El usuario ya existe en el servidor')
        else:
            respuesta = False
            print('El usuario no existe en el servidor')
        return respuesta
    
    @classmethod
    def user_es_propietario(self, id_user, id_server):
        """Metodo para verificar si un usuario existe en un servidor"""
        query = """SELECT * FROM (grupo11.user_server
        INNER JOIN grupo11.usuarios ON user_server.id_user = usuarios.id_user)
        WHERE user_server.id_server = %s and user_server.id_user = %s and user_server.propietario = 1"""
        params = id_server,id_user,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            respuesta = True
            print('El usuario si es propietario del Servidor')
        else:
            respuesta = False
            print('El usuario no es propietario del servidor')
        return respuesta