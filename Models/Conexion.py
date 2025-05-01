import sys
import os

# Añade el directorio raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Logging.logger_test import log


class Conexion:
    #Variables privadas de clase (atributos de clase)
    _DATA_BASE = "test_db" #Nombre de la base de datos
    _USERNAME = "postgres" #Usuario de la base de datos
    _PASSWORD = "admin" #Contraseña de la base de datos
    _PUERTO = "5432" #Puerto de la base de datos
    _HOST = "127.0.0.1" #Host de la base de datos
    _conexion = None #Variable de clase para la conexion a la base de datos
    _cursor = None #Variable de clase para el cursor de la base de datos
    
    #Definimos los metodos
    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                #Importar la libreria psycopg2 para conectarse a la base de datos
                import psycopg2
                
                #Cre el objeto de la conexion a la base de datos
                cls._conexion = psycopg2.connect(
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    host=cls._HOST,
                    port=cls._PUERTO,
                    database=cls._DATA_BASE
                )
                
                log.debug(f"Conectado a la base de datos {cls._DATA_BASE} en {cls._HOST}:{cls._PUERTO}")
                    
                return cls._conexion
                
            except Exception as ex:
                log.error(f"Error al conectar a la base de datos: {ex}")
                #Si existe un error, terminamos el programa
                sys.exit()
        else:
            #Si el objetro no es None, ya existe
            return cls._conexion
        
        
    #DEFINIMOS EL METODO PARA OBTENER EL CURSOR DE LA BASE DE DATOS
    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            #Si el cursor es None, creamos el cursor
            try:
                cls._cursor = cls.obtenerConexion().cursor() #Obtenemos el cursor de la conexion
                log.debug(f"Cursor creado: {cls._cursor}")
                
                return cls._cursor #Retornamos el cursor                
                
            except Exception as ex:
                log.error(f"Error al crear el cursor: {ex}")
                #Si existe un error, terminamos el programa
                sys.exit()
        else:
            #Si el cursor no es None, ya existe
            return cls._cursor 
        
# Probar la clase Conexion
if __name__ == "__main__":
    #Probar la conexion a la base de datos
    Conexion.obtenerConexion()
    
    #Probar el cursor de la base de datos
    Conexion.obtenerCursor()