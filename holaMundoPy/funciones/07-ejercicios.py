"""
un palindromo es una palabra que se lee igual de
izquierda a derecha que de derecha a izquierda
ejemplo: oso, reconocer, rotor, abba, etc
"""


def es_palindromo(texto):
    texto = str(texto.replace(" ", ""))
    reves = al_reves(texto.replace(" ", ""))
    if texto.lower() == reves.lower():
        return True
    else:
        return False


def al_reves(texto):
    return texto[::-1]


print("Abba", es_palindromo("Abba"))  # debe inficar que es verdadero(true)
print("Oso", es_palindromo("Oso"))  # debe inficar que es verdadero(true)
# debe inficar que es verdadero(true)
print("Amo la paloma", es_palindromo("Amo la paloma"))
# debe inficar que es falso("false")
print("Hola Mundo", es_palindromo("Hola Mundo"))

# código para quitar espacios en blanco de una cadena
# texto = "Hola Mundo"
# print(texto.replace(" ", ""))  # HolaMundo
# tex
