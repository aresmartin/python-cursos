"""
    Escribe un programa en Python que acepte una secuencia de números,
    y cuando el usuario teclee un cero calcule su media,
    mayor, menor, y su desviación típica 
    (el último cero no debe estar incluido en los cálculos).
"""

from math import sqrt

resultado = ""
valores = []


def calcular_media(valores):
    suma = 0
    for valor in valores:
        suma = suma + valor
    return suma/(len(valores) - 1)


def calcular_mayor(valores):
    mayor = 0
    for valor in valores:
        if mayor < valor:
            mayor = valor
    print("El mayor valor introducido es: ", str(mayor))


def calcular_menor(valores):
    menor = 999
    valores.pop()

    for valor in valores:
        if menor > valor:
            menor = valor
    print("El menor valor introducido es: ", str(menor))


def desviacion_tipica(valores, media):
    suma = 0
    desviacion = ""
    for valor in valores:
        suma += (valor - media) ** 2
    radicando = suma / (len(valores) - 1)
    return sqrt(radicando)


while True:
    resultado = input("Inserte un número: ")
    resultado = int(resultado)
    valores.append(resultado)
    if resultado != 0 and resultado > 0:
        continue
    else:
        media = calcular_media(valores)
        print(f"La media es {media}")
        calcular_mayor(valores)
        calcular_menor(valores)
        desviacion = desviacion_tipica(valores, media)
        print(f"La desviacion tipica es {desviacion}")
        break
