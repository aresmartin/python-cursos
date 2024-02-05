saludo = 25  # Variables globales -> mala practica


def saludar():
    global saludo  # Variable global
    saludo = "Hola Mundo"


def saludaChanchito():
    saludo = "Hola Chanchito"
    print(saludo)


resultado1 = saludo + 3
print(resultado1)
saludar()
resultado2 = saludo + 3
print(resultado2)

# Razon por la que no se usan variables globales
