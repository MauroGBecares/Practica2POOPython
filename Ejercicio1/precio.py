from estadia import Estadia

class Precio:
    def __init__(self) -> None:
        pass
    
    __precio_hora = 100

        
    @classmethod
    def calcular_importe(cls, cant_horas):
        return cant_horas * cls.__precio_hora


    