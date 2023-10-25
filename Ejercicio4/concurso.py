from datetime import date
from inscripcion import Inscripcion
from titulo import Titulo

class Concurso:
    def __init__(self, nombre: str, fecha_inscripcion_desde: date, fecha_inscripcion_hasta: date, titulo: Titulo) -> None:
        self.__nombre = nombre
        self.__fecha_inscripcion_desde = fecha_inscripcion_desde
        self.__fecha_inscripcion_hasta = fecha_inscripcion_hasta
        self.__titulo = titulo
        self.__inscripciones = []

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre

    @property
    def fecha_inscripcion_desde(self) -> date:
        return self.__fecha_inscripcion_desde
    
    @fecha_inscripcion_desde.setter
    def fecha_inscripcion_desde(self, nueva_fecha: date):
        self.__fecha_inscripcion_desde = nueva_fecha

    @property
    def fecha_inscripcion_hasta(self) -> date:
        return self.__fecha_inscripcion_hasta
    
    @fecha_inscripcion_hasta.setter
    def fecha_inscripcion_hasta(self, nueva_fecha: date):
        self.__fecha_inscripcion_hasta = nueva_fecha

    @property
    def inscripciones(self) -> list:
        return self.__inscripciones
    
    @inscripciones.setter
    def inscripciones(self, nuevas_inscripciones: list):
        self.__inscripciones = nuevas_inscripciones

    @property
    def titulo(self) -> Titulo:
        return self.__titulo
    
    @titulo.setter
    def titulo(self, nuevo_titulo: Titulo):
        self.__titulo = nuevo_titulo

    def __str__(self) -> str:
        return f"El concurso es: {self.nombre}"
    
    def add_inscripcion(self, inscripcion: Inscripcion):
        self.inscripciones.append(inscripcion)
    
    def remove_inscripcion(self, inscripcion: Inscripcion):
        self.inscripciones.remove(inscripcion)

    def get_inscripciones_activas(self) -> list:
        return [inscripcion for inscripcion in self.inscripciones if inscripcion.inscripcion_activa]