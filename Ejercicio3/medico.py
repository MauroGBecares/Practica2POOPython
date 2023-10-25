from datetime import date
from especialidad import Especialidad

class Medico():
    def __init__(self, nombre_apellido: str, matricula: str, fecha_matricula: date) -> None:
        self.__nombre_apellido = nombre_apellido
        self.__matricula = matricula
        self.__fecha_matricula  = fecha_matricula
        self.__especialidades = []

    @property
    def nombre_apellido(self) -> str:
        return self.__nombre_apellido
    
    @property
    def matricula(self) -> str:
        return self.__matricula
    
    @property
    def fecha_matricula(self) -> str:
        return self.__fecha_matricula
    
    @property
    def especialidades(self) -> list:
        return self.__especialidades
    
    @especialidades.setter
    def especialidades(self, especialidades: list):
        self.__especialidades = especialidades
    
    @nombre_apellido.setter
    def nombre(self, nombre):
        self.__nombre_apellido = nombre
    
    @matricula.setter
    def matricula(self, mat):
        self.__matricula = mat
    
    @fecha_matricula.setter
    def fecha_matricula(self, fecha):
        self.__fecha_matricula = fecha

    def __str__(self) -> str:
        return f"Matricula: {self.matricula} - Nombre y Apellido: {self.nombre_apellido}"

    def agregar_especialidad(self, especidalidad_ingresada: Especialidad):
        self.especialidades.append(especidalidad_ingresada)

    def eliminar_especialidad(self, especidalidad_ingresada: Especialidad):
        for especialidad in self.especialidades:
            if especialidad == especidalidad_ingresada:
                self.especialidades.pop(especialidad)

medico1 = Medico("Jose Ramirez", "56547", date(2022,6,2))