from datetime import *
from paciente import *
from medico import *


class Turno:
    def __init__(self, fecha: date, hora: time, paciente: object, medico: object) -> None:
        self.__fecha = fecha
        self.__hora = hora
        self.__estado = 'Reservado'
        self.__autorizado = False
        self.__paciente = paciente
        self.__medico = medico 

    @property
    def fecha(self):
        return self.__fecha
    
    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @property
    def hora(self):
        return self.__hora
    
    @hora.setter
    def hora(self, hora):
        self.__hora = hora

    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @property
    def paciente(self) -> object:
        return self.__paciente
    
    @paciente.setter
    def paciente(self, paciente: object):
        self.__paciente = paciente

    @property
    def autoriado(self) -> bool:
        return self.__autorizado
    
    @autoriado.setter
    def autorizado(self, autorizado: bool):
        self.__autorizado = autorizado

    @property
    def medico(self) -> object:
        return self.__medico
    
    @medico.setter
    def medico(self, medico: object):
        self.__medico = medico

    def __str__(self) -> str:
        return self.fecha
    def ingresar_paciente(self, token: int) -> bool:
        if len(token) == 4: 
            self.estado = 'Ingresado'
            self.autoriado = True
            return True
        return False  
    
    def cancelar_turno(self) -> None:
        self.estado = "Cancelado"