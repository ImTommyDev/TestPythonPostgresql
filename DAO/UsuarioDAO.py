import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Models.Conexion import Conexion
from Models.Usuario import Usuario
from Logging.logger_test import log

class UsuarioDAO:
    '''
    DAO (Data Access Object) para la entidad Usuario.
    Proporciona métodos para interactuar con la base de datos y realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en la tabla de usuarios.
    '''
    _SELECT = 'SELECT * FROM usuarios ORDER BY id_usuario'
    _SELECT_BY_ID = 'SELECT * FROM usuarios WHERE id_usuario=%s'
    _INSERT = 'INSERT INTO usuarios(nombre, edad, email) VALUES(%s, %s, %s)'
    _UPDATE = 'UPDATE usuarios SET nombre=%s, edad=%s, email=%s WHERE id_usuario=%s'
    _DELETE = 'DELETE FROM usuarios WHERE id_usuario=%s'
    
    @classmethod
    def seleccionar(cls):
        #Obtenengo el cursor de la base de datos 
        with  Conexion.obtenerCursor() as cursor: #El cursor ya llama al metodo de obtenerConexion
            
            cursor.execute(cls._SELECT) #Ejecutamos la consulta
            registros = cursor.fetchall()
            
            #Creo una lista de usuarios
            usuarios = []
            
            #Muestro los registros obtenidos, cada registro es un usuario
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2], registro[3])
                usuarios.append(usuario)
                
            return usuarios
        
    #Método para insertar un usuario
    @classmethod
    def insertar(cls, usuario):
        #Creo una transaccion
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (usuario.nombre, usuario.edad, usuario.email)
                cursor.execute(cls._INSERT, valores)
                log.debug(f'Usuario a insertar: {usuario}')

                return cursor.rowcount #Retorno el numero de filas afectadas (1 si se inserto correctamente, 0 si no se inserto)

if __name__ == '__main__':
    
    #Simular un select
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
    
    
    #Simular un insert
    usuario1 = Usuario(nombre="Juan", edad=25, email="juanitoooo@gmail.com")
    UsuarioDAO.insertar(usuario1)