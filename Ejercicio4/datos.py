from concurso import Concurso
from datetime import date
from titulo import Titulo

medicina = Titulo("Medico", 5487)
ingeniero_civil = Titulo("Ingeniero Civil", 6654)


titulos = [medicina, ingeniero_civil]

profesionales = []

concursos = [Concurso("Ingenieria", date(2022, 6, 5), date(2022, 8, 20), ingeniero_civil), Concurso("Medicina", date(2023, 4, 15), date(2023, 9, 22), medicina)]

