from ..models.usuario_model import Usuario
from flask import request, session
from ..models.exceptions import UserNotFound, InvalidDataError


class UsuarioController:

    @classmethod
    def bienvenida(self):
        return "bienvenidos al desarrollo TIF - Somos el Grupo 11"
    
    @classmethod
    def login(cls):
        data = request.json
        login_user = Usuario(
            user = data.get('user'),
            password = data.get('password')
        )
        # Primero verificamos si el usuario existe en la base de datos
        existe_usuario = Usuario.existe_user(login_user)
        if existe_usuario == True:
            # Luego verificamos si la contraseña es correcta
            if Usuario.is_registered(login_user):
                session['user'] = data.get('user')
                return {"message": f"Sesion iniciada usuario {login_user.user}"}, 200
            else:
                return {"message": "La contraseña especificada NO ES CORRECTA!!!"}, 401
                # raise UserNotFound(404,f"Constraseña Incorrecta usuario **{login_user.user}**",f'La contraseña especificada NO es correcta !!!.')
                
        # raise UserNotFound(404,"Usuario Incorrecto",f'El nombre de usuario **{login_user.user}** NO existe, debera especificar otro !!!.')
        return {"message": f"El usuario {login_user.user} NO EXISTE!!!, verifique este dato."}, 401
        
    @classmethod
    def show_profile(cls):
        username = session.get('user')
        print(username)
        user = Usuario.get_user(Usuario(user = username))
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return user.serialize(), 200
    
    @classmethod
    def logout(cls):
        session.pop('user', None)
        return {"message": "Sesion cerrada"}, 200

    @classmethod
    def buscar_usuario(cls, id_user):
        """Metodo para buscar un usuario por su id"""
        user = Usuario(id_user=id_user)
        result = Usuario.get_user(user)
        if result is not None:
            return result.serialize(), 200
        else:
            return {'message': f'No se encontro al usuario solicitado !!!'}, 400

    @classmethod
    def listar_usuarios(cls):
        """Listar todos los usuarios"""
        user_objects = Usuario.get_users()
        usuarios = []
        for user in user_objects:
            usuarios.append(user.serialize())
        return usuarios, 200

    @classmethod
    def crear_usuario(cls):
        """Create a new user"""
        data = request.json

        # Control de datos obligatorios
        if 'nombre' not in data:
            raise InvalidDataError(400,'Invalid Data Error','El nombre es un dato obligatorio, Debe ingresarlo !!!')
        
        if 'apellido' not in data:
            raise InvalidDataError(400,'Invalid Data Error','El Apellido un dato obligatorio, Debe ingresarlo !!!')
        
        if 'user' not in data:
            raise InvalidDataError(400,'Invalid Data Error','Debe especificar un nombre de Usuario !!!')
        
        if 'password' not in data:
            raise InvalidDataError(400,'Invalid Data Error','Debe especificar una contraseña !!!')
        
        if 'preg_secret' not in data:
            raise InvalidDataError(400,'Invalid Data Error','Debe especificar una Pregunta secreta, Debe ingresarla !!!')
        
        if 'respuesta' not in data:
            raise InvalidDataError(400,'Invalid Data Error','Debe especificar una Respuesta, para su pregunta secreta')
        

        nuevo_usuario = Usuario(
            nombre = data.get('nombre'),
            apellido = data.get('apellido'),
            email = data.get('email'),
            user = data.get('user'),
            password = data.get('password'),
            f_nac = data.get('f_nac'),
            #avatar = data.get('avatar'),
            preg_secret = data.get('preg_secret'),
            respuesta = data.get('respuesta')
        )

        newuser = data.get('user')

        # Verificamos si ya existe el nombre de usuario cargado en el sistema
        disponible = Usuario.existe_usuario(newuser)
        if disponible == True:
            Usuario.create_user(nuevo_usuario)
            return {'message': f'Se registro correctamente al usuario {newuser}'}, 200
        else:
            #raise UserNotFound(404,"User Not Found",f'El nombre de usuario **{newuser}** NO ESTA DISPONIBLE, debera especificar otro !!!.')
            return {'message': f'El nombre de usuario **{newuser}** NO ESTA DISPONIBLE, debera especificar otro !!!'}, 404
        

    @classmethod
    def update_usuario(self):
        data = request.json
        usuario = Usuario(
            id_user = data.get('id_user'),
            nombre = data.get('nombre'),
            apellido = data.get('apellido'),
            email = data.get('email'),
            user = data.get('user'),
            password = data.get('password'),
            f_nac = data.get('f_nac'),
            #avatar = data.get('avatar'),
            preg_secret = data.get('preg_secret'),
            respuesta = data.get('respuesta')
        )
        # Verificamos si ya existe el nombre de usuario cargado en el sistema
        existe_usuario = Usuario.existe_user(usuario)
        if existe_usuario == True:
            Usuario.update_user(usuario)
            return {'message': f'Se actualizo correctamente al usuario = {usuario.user}'}, 200
        else:
            #raise UserNotFound(404,"User Not Found",f'El usuario con id = {id_user} NO existe, verifique el dato !!!.')
            return {"message": f"El usuario {usuario.user} NO EXISTE!!!, verifique este dato."}, 401

    @classmethod
    def delete_usuario(cls, id_user):
        """Delete Usuario"""
        usuario = Usuario(id_user=id_user)
        # Validamos si el usuario existe
        existe_usuario = Usuario.existe_iduser(usuario.id_user)
        if existe_usuario == True:
            Usuario.delete_user(usuario)
            return {'message': f'Se ELIMINO correctamente el Usuario con id = {id_user}'}, 200
        else:
            raise UserNotFound(404,"User Not Found",f"El Usuario con id = {id_user} NO EXISTE, verifique este dato!!!")
        

    @classmethod
    def verificar_respuesta(self):
        """Metodo para verifcar si la respuesta ingresada es correcta"""
        data = request.json
        usuario = Usuario(
            user = data.get('user'),
            respuesta = data.get('respuesta')
        )
        # Primero verificamos si el usuario existe en la base de datos
        existe_usuario = Usuario.existe_user(usuario)
        if existe_usuario == True:
            # Luego verificamos si la respuesta ingresada es correcta
            if Usuario.verificar_pregunta(usuario):
                return {"message": f"Respondio Correctamente"}, 200
            else:
                return {"message": "La respuesta especificada NO ES CORRECTA!!!"}, 401
                # raise UserNotFound(404,f"Constraseña Incorrecta usuario **{login_user.user}**",f'La contraseña especificada NO es correcta !!!.') 
        # raise UserNotFound(404,"Usuario Incorrecto",f'El nombre de usuario **{login_user.user}** NO existe, debera especificar otro !!!.')
        return {"message": f"El usuario {usuario.user} NO EXISTE!!!, verifique este dato."}, 401

        
        
        


        
    