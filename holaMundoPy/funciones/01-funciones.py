def hola(nombre, apellido="Feliz"):  # Parametro por defecto
    print("Hola Mundo")
    print(f"Bienvenido {nombre} {apellido}")


hola("Juan")
hola("Pedro", "Perez")


hola(apellido="Ares", nombre="Martin")  # ponemos argumentos al revés
