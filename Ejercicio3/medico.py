from datetime import date
from especialidad import *

class Medico():
    def _init_(self, nombre_apellido: str, matricula: str, fecha_mat: date) -> None:
        self.__nombre_apellido = nombre_apellido
        self.__matricula = matricula
        self.__fecha_mat  = fecha_mat
        self.__especialidades = []

    @property
    def nombre(self) -> str:
        return self.__nombre_apellido
    @property
    def mat(self) -> str:
        return self.__matricula
    @property
    def fecha(self) -> str:
        return self.__fecha_mat
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre_apellido = nombre
    
    @mat.setter
    def mat(self, mat):
        self.__matricula = mat
    
    @fecha.setter
    def fecha(self, fecha):
        self.__fecha_mat = fecha

    @property
    def especialidades(self):
        return self.__especialidades
    
    @especialidades.setter
    def especialidades(self, especialidad: object):
        self.__especialidades = especialidad

    def agregar_especialidad(self, nueva_especialidad):
        self.especialidades.append(nueva_especialidad)

    def eliminar_especialidad(self, especialidad_a_eliminar):
        for especialidad in self.especialidades: 
            if especialidad == especialidad_a_eliminar:
                self.especialidades.pop(especialidad_a_eliminar)

    def __str__(self) -> str:
        return self.nombre_apellido