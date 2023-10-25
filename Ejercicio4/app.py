from datos import *
from inscripcion import Inscripcion
from profesional import Profesional

def mensaje_bienvenida():
    print("Bienvenido/a al sistema de inscripción a concursos para profesionales !!")

def menu_principal():
    print("Que desea realizar: ")
    print("1 - Inscribirse a un concurso")
    print("2 - Cancelar inscripción")
    print("3 - Registrar profesional")

def mostrar_concursos() -> Concurso:
    concursos_disponibles = {}
    for i, concurso in enumerate(concursos, 1):
        print(f"{i} - {concurso.nombre}")
        concursos_disponibles[str(i)] = concurso
    opt_concurso = input("Ingrese el concurso en el cual desea inscribirse: ")
    if opt_concurso.isnumeric() or 1 < opt_concurso > len(concursos_disponibles):
        return concursos_disponibles[str(opt_concurso)]
    return None

def registrar_profesional(respuesta):
    while True:
        if respuesta == "S":
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            dni = input("Ingrese su dni: ")
            if validar_dni(dni) is None:
                nuevo_profesional = Profesional(nombre, apellido, dni)
                profesionales.append(nuevo_profesional)
                agregar_titulos(nuevo_profesional)
                print("El registro ha sido completado exitosamente !!")
                break
            else:
                print("El dni ingresado ya se encuentra registrado. Vuelva a ingresar los datos.")
                continue
        elif respuesta == "N":
            return
        else:
            print("La respuesta ingresada es inválida. Debe ingresar 'S' de Si o 'N' de No")

def agregar_titulos(profesional):
    for titulo in titulos:
        print(f"Cod: {titulo.codigo} - Titulo: {titulo.nombre}")
    opt_titulo = input("Ingrese el código del titulo que desea agregar: ")
    while True:
        agregado = False
        for titulo in titulos:
            if titulo.codigo == int(opt_titulo):
                profesional.titulos.append(titulo)
                print("Agregando...")
                agregado = True
        if agregado:
            print("El titulo se agrego exitosamente.")
        else:
            print("El código ingresado no pertenece a un título cargado en el sistema")
        opt_titulo = input("Ingrese otro código para agregar mas titulos o ingrese 'salir' para dejar de agregar: ")
        if opt_titulo.lower() == "salir":
            return

def validar_titulo_profesional(concurso, profesional):
    for titulo_profesional in profesional.titulos:
        if titulo_profesional == concurso.titulo:
            return True
    return False

def validar_dni(dni):
    for profesional in profesionales:
        if dni == profesional.nro_documento:
            return profesional
    return None

def listar_inscripciones_profesional(profesional):
    if len(profesional.inscripciones) != 0:
        for inscripcion in profesional.inscripciones:
            print(f"Nro inscripcion: {inscripcion.nro} - Fecha: {inscripcion.fecha_hora_inscripcion}")
            return True
    else:
        return False

def cancelar_inscripcion():
    dni_ingresado = input("Ingrese su DNI: ")
    profesional = validar_dni(dni_ingresado)
    if profesional is not None:
        if listar_inscripciones_profesional(profesional):
            opt_inscripcion = input("Ingrese el número de la inscripcion que desea cancelar: ")
            for inscripcion in profesional.inscripciones:
                if int(opt_inscripcion) == inscripcion.nro:
                    inscripcion.inscripcion_activa = False
                    print(inscripcion)
        else:
            print("No tiene inscripciones activas")
    else:
        print("El dni ingresado no es encuetra registrado.")

def nueva_inscripcion():
    concurso_elegido = mostrar_concursos()
    if concurso_elegido is not None:
        dni = input("Ingrese el nro de documento: ")
        profesional = validar_dni(dni)
        if profesional is not None:
            if validar_titulo_profesional(concurso_elegido, profesional):
                nueva_inscripcion = Inscripcion()
                profesional.inscripciones.append(nueva_inscripcion)
                concurso_elegido.add_inscripcion(nueva_inscripcion)
                print("Usted se ha inscripto al concurso exitosamente !!")
            else:
                print(f"El curso requiere el titulo: {concurso_elegido.titulo.nombre} y por lo tanto no puede inscribirse")
        else:
            respuesta = input("Usted no se encuentra registrado. Desea registrarse?(S/N): ")
            registrar_profesional(respuesta.upper())
    else:
        print("No hay concursos para inscribirse.")

mensaje_bienvenida()
while True:
    menu_principal()
    opt = input("Ingrese una opción: ")
    if opt == "1":
        nueva_inscripcion()
    if opt == "2":
        cancelar_inscripcion()
    if opt == "3":
        registrar_profesional("S")
    if opt == "4":
        print("Saludos!.")
        break