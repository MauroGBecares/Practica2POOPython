from datetime import date
from provincia import Provincia

class Pais:
    __codigos_disponibles = set()

    def __init__(self, nombre: str, codigo: int) -> None:
        if codigo in Pais.__codigos_disponibles:
            raise ValueError("El codigo ingresado ya existe.")
        self.__nombre = nombre
        self.__codigo = codigo
        self.__fecha_alta = date.today()
        self.__provincias = []
        Pais.__codigos_disponibles.add(codigo)
    
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
    def provincias(self) -> list:
        return self.__provincias
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    def __str__(self) -> str:
        return self.nombre
    
    def add_provincia(self, provincia: Provincia):
        self.__provincias.append(provincia)
    
    def remove_provincia(self, provincia: Provincia):
        if provincia in self.__provincias:
            self.__provincias.remove(provincia)