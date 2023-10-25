from especialidad import Especialidad
from medico import Medico
from datetime import date

especialidad1 = Especialidad("Psicologia", 5646)
especialidad2 = Especialidad("Pedriatria", 5468)
especialidad3 = Especialidad("Oftamologia", 1324)

especialidades = [especialidad1, especialidad2, especialidad3]

medico1 = Medico("Jose Ramirez", "56547", date(2022,6,2))
medico2 = Medico("Jose Perez", "56647", date(2003,10,3))
medico1.agregar_especialidad(especialidad1)
medico2.agregar_especialidad(especialidad2)
medico2.agregar_especialidad(especialidad3)

medicos = [medico1, medico2]

turnos = []