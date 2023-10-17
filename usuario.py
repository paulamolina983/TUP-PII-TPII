from estudiante import *


class Usuario(Estudiante):
    #Tengo dudas si es con doble guion bajo o con solo uno
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        super().__init__()
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contrasenia = contrasenia

    @property
    #¿aca se ponia nombre o __nombre?
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, nuevo_apellido):
        self.__apellido = nuevo_apellido

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, nuevo_email):
        self.__email = nuevo_email
    
    @property
    def contrasenia(self):
        return self.__contrasenia
    
    @contrasenia.setter
    def contrasenia(self, nuevo_contrasenia):
        self.__contrasenia = nuevo_contrasenia