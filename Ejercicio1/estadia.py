from datetime import *
from precio import Precio

class Estadia:
    def __init__(self, nro_patente: str, hora_entrada:time=datetime.now().strftime("%H:%M")) -> None:
        self.__fecha = date.today()
        self.__nro_patente = nro_patente
        self.__hora_entrada = hora_entrada
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
        formato = "%H:%M"
    
        try:
            hora_entrada = datetime.strptime(self.hora_entrada, formato)
            hora_salida = datetime.strptime(self.hora_salida, formato)
        
            diferencia = hora_salida - hora_entrada
            horas_totales = diferencia.total_seconds() / 3600  # 3600 segundos en una hora
            return horas_totales
        except ValueError:
            return "Formato de hora incorrecto. Debe ser 'HH:MM'."
    
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
    
    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    def __str__(self) -> str:
        return self.nro_patente
        
    def registrar_salida(self):
        self.estado = "Pagado"
        self.hora_salida = datetime.now().strftime("%H:%M")
        precio = Precio.calcular_importe(self.cant_horas)
        return precio