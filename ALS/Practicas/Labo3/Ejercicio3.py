"""
Crea un programa que permita guardar y hacer búsquedas sobre pares de (nombre, e.mail). 
El programa presentará un menú principal, con las opciones introducir, borrar y buscar. 
Al introducir datos, se pide un nombre y un e.mail, y se guardan. Para borrar, sólo se pide el nombre, 
se busca y se borra. Para buscar, sólo se pide el nombre, se busca y se muestra.
Se debe utilizar un diccionario para guardar los datos. Créese una función que pida un nombre y devuelva 
el valor asociado (el métodod get() devuelve None si no se encuentra la clave), como soporte para las otras tres.
¿Puedes crear fácilmente una opción más, listado, que liste todas las entradas (nombre, email)?
"""
usuarios = [
    {"nombre": "Jose", "e.mail": "jose@gmail.com"},
    {"nombre": "Maria", "e.mail": "maria@gmail.com"},
    {"nombre": "Nicolas", "e.mail": "nicolas@gmail.com"},
    {"nombre": "Felipe", "e.mail": "felipe@gmail.com"},
]

while True:
    opcion = input("Elije opción: \nIntroducir. \nBorrar. \nListar. \nBuscar. \nSalir. \n=> ")
    if opcion == "introducir":
        nombre = input("Introduce nombre de un usuario: ")
        email = input("Introduce su e.mail: ")
        usuario = {"nombre": nombre, "e.mail": email}
        accion = usuarios.append(usuario)
        print(f"Usuario {usuario} insertado:\n")
    elif opcion == "borrar":
        usuario = input("Introduzca el usuario que desea borrar: ")
        if usuario in usuarios:            
            accion = usuarios.remove(usuario["nombre"])
            print(f"Usuario {accion} eliminado:\n")

        else:
            print("Usuario no encontrado.")
    elif opcion == "listar":
        for usuario in usuarios:
            print(usuario)
    elif opcion == "buscar":
        nombre = input("Introduce el nombre del usuario que desea buscar: ")

        existe = False
        for usuario in usuarios :
            if usuario["nombre"] == nombre:
                print(f"El usuario {nombre} se ha encontrado")
                existe = True
                break
        if existe == False:
            print("No existe el usuario")
    elif opcion == "salir":
        break

