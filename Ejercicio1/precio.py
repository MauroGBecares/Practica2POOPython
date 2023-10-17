class Precio:
    __precio_hora = 100

    def __init__(self) -> None:
        pass
        
    @classmethod
    def calcular_importe(cls, cant_horas):
        return round(cant_horas) * cls.__precio_hora