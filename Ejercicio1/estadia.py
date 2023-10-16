from datetime import *
from precio import Precio


class Estadia:
    def __init__(self, nro_patente) -> None:
        self.__fecha = date.today()
        self.__nro_patente = nro_patente
        # self.__hora_entrada = str(datetime.now().hour) + ":" + str(datetime.now().minute)
        self.__hora_entrada = None
        self.__cant_horas = None
        self.__estado = "Activo"
        self.__pagado = False
        self.__hora_salida = None

    @property
    def fecha(self):
        return self.__fecha
    
    @property
    def nro_patente(self):
        return self.__nro_patente

    @property
    def hora_entrada(self):
        return self.__hora_entrada
    
    @property
    def cant_horas(self):
        return self.__cant_horas
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def pagado(self):
        return self.__pagado
    
    @property
    def hora_salida(self):
        return self.__hora_salida

    @hora_salida.setter
    def hora_salida(self, hora):
        self.__hora_salida = hora

    def __str__(self) -> str:
        pass

    def registrar_salida(self):
        precio = Precio.calcular_importe()

    
    
    
    def calcular_horas_estadia(entrada, salida):
        formato = "%H:%M"
    
        try:
            hora_entrada = datetime.strptime(entrada, formato)
            hora_salida = datetime.strptime(salida, formato)
        
            diferencia = hora_salida - hora_entrada
            horas_totales = diferencia.total_seconds() / 3600  # 3600 segundos en una hora
            return horas_totales
        except ValueError:
            return "Formato de hora incorrecto. Debe ser 'HH:MM'."