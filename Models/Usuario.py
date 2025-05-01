import sys
import os

# Añade el directorio raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Logging.logger_test import log

class Usuario:
    def __init__(self, id_usuario = None, nombre = None, edad = None, email = None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.edad = edad
        self.email = email
        
    def __str__(self):
        return f"Usuario [id_usuario={self.id_usuario}, nombre={self.nombre}, edad={self.edad}, email={self.email}]"
    
    #definimos los metodos get y set para cada atributo de la clase
    @property #Metodo get
    def id_usuario(self):
        return self._id_usuario
    @id_usuario.setter #Metodo set
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario
        
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad
        
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email
        
if __name__ == "__main__":
    usuario1 = Usuario(nombre="Juan", edad=25, email="juan@gmail.com")
    log.debug(usuario1)
    
    #Simular un insert
    usuario2 = Usuario(nombre="Maria",edad=30, email="mario@gmail.com")
    log.debug(usuario2)
    
    #Simular un delete
    usuario3 = Usuario(id_usuario=4)
    log.debug(usuario3)