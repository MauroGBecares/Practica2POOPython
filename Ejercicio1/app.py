from estadia import Estadia

estadias = set()


def menu_principal():
    print("1 - Ingresar estadia")
    print("2 - Finalizar Estadia")
    print("3 - Salir")

def buscar_pantente(patente):
    for estadia in estadias:
        if estadia.nro_patente == patente:
            return estadia, True
    return "", False

while True:
    menu_principal()
    opt = input("Ingrese una opción: ")
    if opt == "1":
        patente = input("Ingrese el nro de patente que desea registrar: ")
        estadia, validacion = buscar_pantente(patente)
        if validacion:
            print("La patente ingresada ya se encuetra registrada.")
            continue
        nueva_estadia = Estadia(patente, "15:30")
        estadias.add(nueva_estadia)
        print(f"La estadia se encuentra registrada - Nro Patente: {nueva_estadia}")
    if opt == "2":
        patente_salida = input("Ingrese el nro de patente que desea finalizar estadia: ")
        estadia, validacion = buscar_pantente(patente_salida)
        if not validacion:
            print("La patente que desea dar de baja no se encuetra registrada")
            continue
        if estadia.estado == "Pagado":
            print("")
            continue
        precio = estadia.registrar_salida()
        print(f"Se registro la salida del vehiculo. El costo es: {precio}")
    if opt == "3":
        print("Saludos!.")
        break