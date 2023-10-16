from datetime import date
from localidad import Localidad

class Provincia:
    __codigos_disponibles = set()

    def __init__(self, nombre: str, codigo: int) -> None:
        if codigo in Provincia.__codigos_disponibles:
            raise ValueError("El codigo existe, ingrese otro.")
        self.__nombre = nombre
        self.__codigo = codigo
        self.__fecha_alta = date.today()
        self.__localidades = []
        Provincia.__codigos_disponibles.add(codigo)
    
    @property
    def nombre(self) -> str: 
        return self.__nombre
    
    @property
    def codigo(self) -> int:
        return self.__codigo
    
    @property
    def fecha_alta(self) -> date:
        return self.__fecha_alta
    
    @property
    def localidades(self) -> list:
        return self.__localidades

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre

    def __str__(self) -> str:
        return self.nombre
    
    def add_localidad(self, localidad: Localidad):
        self.__localidades.append(localidad)

    def remove_localidad(self, localidad: Localidad):
        if localidad in self.localidades:
            self.__localidades.remove(localidad)