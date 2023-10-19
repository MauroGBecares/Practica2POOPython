class Especialidad:
    def _init_(self, nombre: str, codigo: int) -> None:
        self.__nombre = nombre
        self.__codigo = codigo

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

    def _str_(self) -> str:
        return self.nombre