from datetime import date

class Paciente:
    __dni_ingresados = set()

    def __init__(self, nombre_apellido: str, nro_documento: str, direccion: str, fecha_nacimiento: date) -> None:
        if nro_documento in Paciente.__dni_ingresados:
            raise ValueError("El dni ingresado ya se encuentra registrado.")
        self.__nombre_apellido = nombre_apellido
        self.__nro_documento = nro_documento
        self.__direccion = direccion
        self.__fecha_nacimiento = fecha_nacimiento
        Paciente.__dni_ingresados.add(nro_documento)

    @property
    def nombre_apellido(self) -> str:
        return self.__nombre_apellido
    
    @nombre_apellido.setter
    def nombre_apellido(self, nuevo_nombre_apellido) -> None:
        self.__nombre_apellido = nuevo_nombre_apellido

    @property 
    def nro_documento(self) -> str:
        return self.__nro_documento
    
    @nro_documento.setter
    def nro_documento(self, nuevo_documento: str) -> None:
        if nuevo_documento in Paciente.__dni_ingresados:
            raise ValueError("El dni ingresado ya se encuentra registrado.")
        self.__nro_documento = nuevo_documento
    
    @property
    def direccion(self) -> str:
        return self.__direccion
    
    @direccion.setter
    def direccion(self, nueva_direccion: str) -> None:
        self.__direccion = nueva_direccion

    @property
    def fecha_nacimiento(self) -> date:
        return self.__fecha_nacimiento
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, nueva_fecha) -> None:
        self.__fecha_nacimiento = nueva_fecha

    @property
    def edad(self) -> int:
        return date.today().year - self.__fecha_nacimiento
    
    def __str__(self) -> str:
        return self.nombre_apellido

paciente = Paciente("Lopez", "566655", "Pje Manaos 4587", date(2003,9,4))
