from datos import *
from cliente import Cliente

clientes = []

def menu_principal():
    print("-------------------------------------------------------------")
    print("Bienvenido a Soluciones SA")
    print("Ingrese la tarea que desea realizar: ")
    print("1- Registrar cliente")
    print("2- Buscar cliente")
    print("3- Salir")
    return int(input())

def menu_cliente(cliente):
    print(f"Usted esta modificando el cliente {cliente} - Que desea hacer?")
    print("1- Modificar dirección")
    print("2- Eliminar cliente")
    print("3- Reactivar cliente")
    print("4- Salir del menú del cliente")
    return int(input())

def buscar_pais(pais_ingresado):
    for pais in paises:
        if pais.nombre == pais_ingresado:
            return pais, True
    return "El pais ingresado no se encuentra disponible", False

def buscar_provincia(provincia_ingresada, pais):
    for provincia in pais.provincias:
        if provincia.nombre == provincia_ingresada:
            return provincia, True
    return "La provincia ingresada no es encuentra el dicho pais", False

def buscar_localidad_segun_provincia(localidad_ingresada, provincia):
    for localidad in provincia.localidades:
        if localidad.nombre == localidad_ingresada:
            return localidad, True
    return "La localidad ingresada no es encuentra en dicha provincia", False
        
def buscar_cliente(nro_cliente) -> Cliente:
    for cliente in clientes:
        if nro_cliente == cliente.nro_cliente:
            return cliente, True
    return "El cliente que desea encontrar no existe.", False

def buscar_localidad(localidad_ingresada):
    for localidad in localidades:
        if localidad.nombre == localidad_ingresada:
            return localidad, True
    return "La localidad ingresada no es encuentra disponible", False

while True:
    opcion = menu_principal()
    if opcion == 1:
        print("Bienvenido al registro !!")
        nombre_apellido = input("Ingrese el nombre y apellido del cliente: ")
        pais_ingresado = input("Ingrese el pais: ")
        pais, verificacion = buscar_pais(pais_ingresado)
        if not verificacion:
            print(pais)
            continue
        provincia_ingresada = input("Ingrese la provincia: ")
        provincia, verificacion = buscar_provincia(provincia_ingresada, pais)
        if not verificacion:
            print(provincia)
            continue
        localidad_ingresada = input("Ingrese la localidad: ")
        localidad, verificacion = buscar_localidad_segun_provincia(localidad_ingresada, provincia)
        if not verificacion:
            print(localidad)
            continue
        direccion = input("Ingrese la dirección del cliente: ")
        nuevo_cliente = Cliente(nombre_apellido, direccion, localidad)
        clientes.append(nuevo_cliente)
        print(f"El cliente {nuevo_cliente} se agrego exitosamente !")
    elif opcion == 2:
        nro_cliente_ingresado = int(input("Ingrese el nro de cliente que desea encontrar: "))
        cliente, verificacion = buscar_cliente(nro_cliente_ingresado)
        if not verificacion:
            print(cliente)
            continue
        while True:
            opcion_cliente = menu_cliente(cliente)
            if opcion_cliente == 1:
                localidad_ingresada = input("Ingrese la nueva localidad: ")
                localidad, verificacion = buscar_localidad(localidad_ingresada)
                if not verificacion:
                    print(localidad)
                    continue
                cliente.direccion = input("Ingrese la nueva direccion: ")
                cliente.localidad = localidad
            elif opcion_cliente == 2:
                cliente.eliminar_cliente()
                print(f"El cliente {cliente.nombre_apellido} se dio de baja el dia de hoy. {str(cliente.fecha_baja)}")
            elif opcion_cliente == 3:
                cliente.reactivar_cliente()
                print(f"El cliente {cliente.nombre_apellido} se reactivo correctamente.")
            elif opcion_cliente == 4:
                break
            else:
                print("La opción ingresada es invalida")
    elif opcion == 3:
        break
    else:
        print("La opción ingresada es inválida.")