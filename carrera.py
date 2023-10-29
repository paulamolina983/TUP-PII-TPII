from curso import *

class Carrera():
    def __init__(self, nombre:str, cant_anos: int):
        self.__nombre = nombre
        self.__cant_anos = cant_anos


    @property 
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre


    @property 
    def cant_anos(self):
        return self.__cant_anos
    
    @cant_anos.setter
    def cant_anos(self, nueva_cant_anos):
        self.__cant_anos = nueva_cant_anos

    def __str__(self):
       print("DATOS CARRERA")
       print(f"Nombre: {self.nombre}")
       print(f"Cantidad de años: {self.cant_anos}")
       print("------------")
