from ..database import DatabaseConnection
from .exceptions import UserNotFound, InvalidDataError


class Usuario:
    """Usuario model class"""
    def __init__(self, **kwargs):
        self.id_user = kwargs.get('id_user')
        self.nombre = kwargs.get('nombre')
        self.apellido = kwargs.get('apellido')
        self.email = kwargs.get('email')
        self.user = kwargs.get('user')
        self.password = kwargs.get('password')
        self.f_nac = kwargs.get('f_nac')
        #self.avatar = kwargs.get('avatar')
        self.preg_secret = kwargs.get('preg_secret')
        self.respuesta = kwargs.get('respuesta')

    def serialize(self):
        """Serialize object representation"""
        return {
                "id_user": self.id_user,
                "nombre": self.nombre,
                "apellido": self.apellido,
                "email": self.email,
                "user": self.user,
                "password": self.password,
                "f_nac": self.f_nac,
                "preg_secret": self.preg_secret,
                "respuesta": self.respuesta
        }
    
    @classmethod
    def is_registered(cls, user):
        """Metodo para el login de un usuario"""
        query = """SELECT id_user FROM grupo11.usuarios 
        WHERE user = %s and password = %s"""
        params = user.user,user.password,
        result = DatabaseConnection.fetch_one(query, params=params)
        print(user.user)
        print(user.password)
        if result is not None:
            return True
        else:
            return False
    

    @classmethod
    def get_users(cls):
        query = """SELECT id_user, nombre, apellido, email,
        user, password, f_nac, preg_secret, respuesta
        FROM grupo11.usuarios"""
        results = DatabaseConnection.fetch_all(query)
        usuarios = []
        if results is not None:
            for result in results:
                usuarios.append(Usuario(
                    id_user = result[0],
                    nombre = result[1],
                    apellido = result[2],
                    email = result[3],
                    user = result[4],
                    password = result[5],
                    f_nac = result[6],
                    preg_secret = result[7],
                    respuesta = result[8]            
            ))
        return usuarios
    

    @classmethod
    def get_user(cls,user):

        query = """SELECT id_user, nombre, apellido, email,
        user, password, f_nac, preg_secret, respuesta 
        FROM grupo11.usuarios WHERE user like %s"""
        params = user.user,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return Usuario(
                id_user = result[0],
                nombre = result[1],
                apellido = result[2],
                email = result[3],
                user = result[4],
                password = result[5],
                f_nac = result[6],
                preg_secret = result[7],
                respuesta = result[8]             
            )  
        return None
        # else:   
        #     raise UserNotFound(404,"User Not Found",f"El Usuario con id {user.id_user} NO existe, verifique este dato!!!")
    
    @classmethod
    def update_user(cls, user):
        """Modificar Usuario"""

        allowed_columns = {'nombre', 'apellido', 'email',
                           'user', 'password',
                           'f_nac', 'preg_secret', 'respuesta'}
        query_parts = []
        params = []
        for key, value in user.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(user.user)
        query = "UPDATE grupo11.usuarios SET " + ", ".join(query_parts) + " WHERE user = %s"
        DatabaseConnection.execute_query(query, params=params)
        

    @classmethod
    def create_user(cls, user):
        """Crear Usuario"""

        query = """INSERT INTO grupo11.usuarios (nombre, apellido, email,
        user, password, f_nac, preg_secret, respuesta) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

        params = user.nombre, user.apellido, user.email, \
                 user.user, user.password, user.f_nac, \
                 user.preg_secret, user.respuesta
        cursor = DatabaseConnection.execute_query(query, params=params)

        if cursor.rowcount == 1:
            id_usuario = cursor.lastrowid
            return id_usuario
        
        else:
            raise InvalidDataError(400,'Invalid Data Error','Ingreso datos incorrectos')

    @classmethod
    def delete_user(cls, user):
        """Eliminar Usuario"""

        query = "DELETE FROM grupo11.usuarios WHERE id_user = %s"
        params = user.id_user,
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def existe_usuario(self, dato):
        """Metodo para verificar si ya esta registrado el nombre de usuario en la tabla usuarios"""
        query = """SELECT id_user, nombre, apellido, email,
        user, password, f_nac, preg_secret, respuesta 
        FROM grupo11.usuarios WHERE user like %s"""
        params = dato,
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            respuesta = False
        else:
            respuesta = True
        return respuesta
    
    @classmethod
    def verificar_pregunta(self, user):
        """Metodo para verificar si la respues secreta es correcta"""
        
        query = """SELECT id_user, nombre, apellido, email,
        user, password, f_nac, preg_secret, respuesta 
        FROM grupo11.usuarios WHERE user = %s and respuesta like %s"""
        params = user.user,user.respuesta,
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return True
        else:
            return False
    
    @classmethod
    def existe_iduser(self, id_user):
        """Metodo para verificar si existe el id_user existe"""
        
        query = """SELECT id_user, nombre, apellido, email,
        user, password, f_nac, preg_secret, respuesta 
        FROM grupo11.usuarios WHERE id_user = %s"""
        params = id_user,
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            respuesta = True
            print('si existe')
        else:
            respuesta = False
            print('no existe')
        return respuesta
    
    @classmethod
    def existe_user(self, user):
        """Metodo para verificar si existe el user registrado en la base de datos"""
        
        query = """SELECT id_user, nombre, apellido, email,
        user, password, f_nac, preg_secret, respuesta 
        FROM grupo11.usuarios WHERE user = %s"""
        params = user.user,
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            respuesta = True
        else:
            respuesta = False
        return respuesta
