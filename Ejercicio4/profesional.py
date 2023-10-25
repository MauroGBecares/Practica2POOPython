from titulo import Titulo
from inscripcion import Inscripcion

class Profesional:
    def __init__(self, nombre: str, apellido: str, nro_documento: str) -> None:
        self.__nombre = nombre 
        self.__apellido = apellido
        self.__nro_documento = nro_documento
        self.__titulos = []
        self.__inscripciones = []

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter 
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre
    
    @property
    def apellido(self) -> str:
        return self.__apellido
    
    @nombre.setter 
    def apellido(self, nuevo_apellido: str):
        self.__apellido = nuevo_apellido

    @property
    def nro_documento(self) -> str:
        return self.__nro_documento
    
    @nro_documento.setter
    def nro_documento(self, nuevo_nro_documento) -> str:
        self.__nro_documento = nuevo_nro_documento

    @property
    def titulos(self) -> list:
        return self.__titulos
    
    @titulos.setter
    def titulos(self, titulos: list):
        self.__titulos = titulos

    @property
    def inscripciones(self) -> list:
        return self.__inscripciones

    @inscripciones.setter
    def inscripciones(self, nuevas_inscripciones: list):
        self.__inscripciones = nuevas_inscripciones
        
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

    def add_titulo(self, titulo: Titulo):
        self.titulos.append(titulo)
    
    def remove_titulo(self, titulo: Titulo):
        self.titulos.remove(titulo)