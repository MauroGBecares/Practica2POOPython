from datetime import date
from concurso import Concurso

class Inscripcion:
    __prox_nro = int(0)
    
    def __init__(self) -> None:
        self.__nro = self.__get_nro()
        self.__fecha_hora_inscripcion = date.today()
        self.__inscripcion_activa = True

    @property
    def nro(self) -> int:
        return self.__nro
    
    @property
    def fecha_hora_inscripcion(self) -> date:
        return self.__fecha_hora_inscripcion

    @fecha_hora_inscripcion.setter
    def fecha_hora_inscripcion(self, nueva_fecha: date):
        self.__fecha_hora_inscripcion = nueva_fecha

    @property
    def inscripcion_activa(self) -> bool:
        return self.__inscripcion_activa
    
    @inscripcion_activa.setter
    def inscripcion_activa(self, nuevo_estado: bool):
        self.__inscripcion_activa = nuevo_estado

    def __str__(self) -> str:
        if self.inscripcion_activa:
            return f"La inscripcion {self.nro} se encuentra Activa"
        else:
            return f"La inscripcion {self.nro} se encuentra Inactiva"
        
    def __get_nro(cls) -> int:
        cls.__prox_nro = cls.__prox_nro + 1
        return cls.__prox_nro
    