class Contacto:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class Amigo(Contacto):
    pass

class Trabajo(Contacto):
    def __init__(self, nombre, email, email_empresa):
        super().__init__(nombre, email)
        self.email_empresa = email_empresa

contactos_amigos = {}
contactos_trabajo = {}

def menu_principal():
    while True:
        print("-" * 20)
        print("1. Insertar contacto")
        print("2. Borrar contacto")
        print("3. Buscar contacto")
        print("4. Listar contactos")
        print("5. Salir")
        print("-" * 20)

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            insertar_contacto()
        elif opcion == 2:
            borrar_contacto()
        elif opcion == 3:
            buscar_contacto()
        elif opcion == 4:
            listar_contactos()
        elif opcion == 5:
            break
        else:
            print("Opción no válida.")

def insertar_contacto():
    tipo_contacto = input("¿Qué tipo de contacto quieres insertar? (amigo/trabajo): ")
    nombre = input("Introduce el nombre: ")
    email = input("Introduce el email: ")

    if tipo_contacto == "amigo":
        contacto = Amigo(nombre, email)
        contactos_amigos[nombre] = contacto
    elif tipo_contacto == "trabajo":
        email_empresa = input("Introduce el email de la empresa: ")
        contacto = Trabajo(nombre, email, email_empresa)
        contactos_trabajo[nombre] = contacto
    else:
        print("Tipo de contacto no válido.")

def borrar_contacto():
    nombre = input("Introduce el nombre del contacto a borrar: ")

    if nombre in contactos_amigos:
        del contactos_amigos[nombre]
    elif nombre in contactos_trabajo:
        del contactos_trabajo[nombre]
    else:
        print("Contacto no encontrado.")

def buscar_contacto():
    nombre = input("Introduce el nombre del contacto a buscar: ")

    if nombre in contactos_amigos:
        contacto = contactos_amigos[nombre]
        print(f"Nombre: {contacto.nombre}")
        print(f"Email: {contacto.email}")
    elif nombre in contactos_trabajo:
        contacto = contactos_trabajo[nombre]
        print(f"Nombre: {contacto.nombre}")
        print(f"Email: {contacto.email}")
        print(f"Email empresa: {contacto.email_empresa}")
    else:
        print("Contacto no encontrado.")

def listar_contactos():
    print("**Amigos:**")
    for nombre, contacto in contactos_amigos.items():
        print(f"- {nombre}")

    print("**Trabajo:**")
    for nombre, contacto in contactos_trabajo.items():
        print(f"- {nombre}")

menu_principal()
