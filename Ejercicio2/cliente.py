from datetime import date
from localidad import Localidad

class Cliente:
    __prox_nro_cliente = int(0)

    def __init__(self, nombre_apellido: str, direccion: str, localidad: Localidad) -> None:
        self.__fecha_alta = date.today()
        self.__nro_cliente = Cliente.__get_nro_cliente()
        self.__nombre_apellido = nombre_apellido
        self.__direccion = direccion
        self.__fecha_baja = None
        self.__localidad = localidad

    @property
    def nro_cliente(self) -> int:
        return self.__nro_cliente
    
    @property
    def nombre_apellido(self) -> str:
        return self.__nombre_apellido
    
    @property
    def direccion(self) -> str:
        return self.__direccion
    
    @property
    def fecha_alta(self) -> date:
        return self.__fecha_alta
    
    @property
    def fecha_baja(self) -> date:
        return self.__fecha_baja
    
    @property
    def localidad(self) -> Localidad:
        return self.__localidad
    
    @nombre_apellido.setter
    def nombre_apellido(self, nuevo_nombre: str) -> None:
        self.__nombre_apellido = nuevo_nombre
        
    @direccion.setter
    def direccion(self, nueva_direccion: str) -> None:
        self.__direccion = nueva_direccion

    @fecha_baja.setter
    def fecha_baja(self, nueva_fecha_baja: date) -> None:
        self.__fecha_baja = nueva_fecha_baja

    @localidad.setter
    def localidad(self, nueva_localidad: Localidad) -> None:
        self.__localidad = nueva_localidad
    
    def __str__(self) -> str:
        return self.nombre_apellido
    
    def eliminar_cliente(self) -> None:
        self.fecha_baja = date.today()

    def reactivar_cliente(self) -> None:
        self.fecha_baja = None

    @classmethod
    def __get_nro_cliente(cls) -> int:
        cls.__prox_nro_cliente = cls.__prox_nro_cliente + 1
        return cls.__prox_nro_cliente
    