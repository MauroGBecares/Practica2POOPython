from datetime import date

class Localidad:
    __codigos_disponibles = set()

    def __init__(self, nombre: str, codigo: int, cod_postal: int) -> None:
        if codigo in Localidad.__codigos_disponibles:
            raise ValueError("El codigo existe, ingrese otro.")
        self.__codigo = codigo
        self.__nombre = nombre
        self.__cod_postal = cod_postal
        self.__fecha_alta = date.today()
        Localidad.__codigos_disponibles.add(codigo)

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def codigo(self) -> int: 
        return self.__codigo

    @property
    def cod_postal(self) -> int:
        return self.__cod_postal
    
    @property
    def fecha_alta(self) -> date:
        return self.__fecha_alta
    
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre

    @cod_postal.setter
    def cod_postal(self, nuevo_cod_postal: int):
        self.__cod_postal = nuevo_cod_postal
    
    def __str__(self) -> str:
        return self.nombre
    