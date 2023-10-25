class Titulo:
    __cod_disponible = set()

    def __init__(self, nombre: str, codigo: int) -> None:
        if codigo in Titulo.__cod_disponible:
            raise ValueError("El codigo ya se encuentra cargado. Ingrese otro")
        self.__nombre = nombre
        self.__codigo = codigo
        Titulo.__cod_disponible.add(codigo)

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter 
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre

    @property
    def codigo(self) -> int:
        return self.__codigo
    
    @codigo.setter
    def codigo(self, nuevo_codigo: int):
        self.__codigo = nuevo_codigo

    def __str__(self) -> str:
        return f"El titulo es: {self.nombre}"