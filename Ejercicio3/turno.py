from datetime import *
from paciente import *
from medico import *


class Turno:
    def __init__(self, fecha: date, hora: time, paciente: Paciente, medico: Medico) -> None:
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
    def paciente(self) -> Paciente:
        return self.__paciente
    
    @paciente.setter
    def paciente(self, paciente: Paciente):
        self.__paciente = paciente

    @property
    def autorizado(self) -> bool:
        return self.__autorizado
    
    @autorizado.setter
    def autorizado(self, autorizado: bool):
        self.__autorizado = autorizado

    @property
    def medico(self) -> Medico:
        return self.__medico
    
    @medico.setter
    def medico(self, medico: Medico):
        self.__medico = medico

    def __str__(self) -> str:
        return f"Turno: Paciente{self.paciente.nombre_apellido} - Médico: {self.medico.nombre_apellido} - Fecha: {self.fecha} - Hora: {self.hora}"
    
    def ingresar_paciente(self, token: int) -> bool:
        if len(token) == 4: 
            self.estado = 'Ingresado'
            self.autoriado = True
            return True
        return False  
    
    def cancelar_turno(self) -> None:
        self.estado = "Cancelado"