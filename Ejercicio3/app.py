from datos import *
from datetime import *
from turno import Turno
from paciente import Paciente

def menu_principal():
    print("1 - RESERVAR TURNO PACIENTE")
    print("2 - CANCELAR TURNO PACIENTE")
    print("3 - INGRESAR UN PACIENTE")
    print("4 - SALIR")

def listar_especialidades():
    print("-- Listado de especialidades --")
    for especialidad in especialidades:
        print(especialidad)
    opt_especialidad = input("Ingrese el codigo de la especialidad ")
    while True:
        if opt_especialidad.isnumeric() or opt_especialidad >= 1 and opt_especialidad <= len(opt_especialidad):
            return especialidad
        else:
            opt_especialidad = input("El codigo ingresado no pertenece a la lista. Ingrese uno correcto: ")

def listado_medicos_especialidad(especialidad):
    lista_medicos = []
    print(f"Listado de médicos de la especialidad {especialidad.nombre}: ")
    for medico in medicos:
        if especialidad in medico.especialidades:
            print(medico)
            lista_medicos.append(medico)
    while True:
        opt_matricula = input("Ingrese la matricula del médico en el cual desea atenderse: ")
        for medico in lista_medicos:
            if opt_matricula in medico.matricula:
                return medico
        print(f"La matricula ingresada no se encuetra en la lista de médicos de la especialidad {especialidad.nombre}")

def validar_fecha():
    while True:
        fecha_str = input("Ingrese una fecha (año-mes-día): ")
        año, mes, día = map(int, fecha_str.split('-'))
        fecha = date(año, mes, día)
        dia_semana = fecha.weekday()
        if not dia_semana == 5 or dia_semana == 6:
            return fecha
        print("Los dias sabado y domingo no atiende ningun medico.")

def validar_horario():
    while True:
        hora_str = input("Ingrese la hora del turno: ")
        hora, minuto = map(int, hora_str.split(':'))
        hora = time(hora, minuto)
        if hora >= time('13') and hora <= time('19:30'):
            return time(hora)
        print("En el horario ingresado no pueden atender los médicos.")

def registrar_paciente():
    nombre_paciente = input("Ingrese su nombre y apellido: ")
    dni = input("Ingrese su dni: ")
    direccion = input("Ingrese su direccion: ")
    fecha_str = input("Ingrese una fecha de nacimiento (año-mes-día): ")
    año, mes, día = map(int, fecha_str.split('-'))
    fecha = date(año, mes, día)
    return Paciente(nombre_paciente, dni, direccion, fecha)

def reservar_turno():
    paciente = registrar_paciente()
    especialidad = listar_especialidades()
    medico = listado_medicos_especialidad(especialidad)
    while True:
        fecha = validar_fecha()
        horario = validar_horario()
        for turno in turnos:
            if turno.fecha == fecha or turno.hora == horario:
                print("El turno ingresado no se encuentra disponible.")
                continue
        break    
    turnos.append(Turno(fecha, horario, paciente, medico))


def listar_turnos():
    dni_ingresado = input("Ingrese el dni del paciente: ")
    listado_turnos = {}
    for i, turno in enumerate(turnos, 1):
        if turno.paciente.nro_documento == dni_ingresado and turno.estado == "Reservado":
            print(f"{i} - {turno}")
            listado_turnos[str(i)] = turno
    opt_turno = input("Ingrese el turno que desea cancelar: ")
    return listado_turnos[str(opt_turno)] 


def cancelar_turno():
    turno_seleccionado = listar_turnos()
    turno_seleccionado.estado = "Cancelado"
    print("El turno seleccionado se cancelo exitosamente !!")

def ingresar_paciente():
    turno_seleccionado = listar_turnos()
    token_ingresado = input("Ingrese el token del turno: ")
    while True:
        if not(token_ingresado.isnumeric()) and len(token_ingresado) != 4:
            print("El token ingresado tiene que tener 4 digitos")
        else:
            turno_seleccionado.estado = "Ingresado"
            token_ingresado.autorizado = True
            print("El paciente ya fue ingresado.")
            return

while True:
    menu_principal()
    opt = input("Ingrese una opción: ")
    if opt == "1":
        reservar_turno()
    if opt == "2":
        cancelar_turno()
    if opt == "3":
        ingresar_paciente()
    if opt == "4":
        print("Saludos!.")
        break

print("Adios !!")