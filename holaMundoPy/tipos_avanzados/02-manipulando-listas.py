mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
print(mascotas[0])
mascotas[0] = "Bicho"
print(mascotas[0])

# izquierda es para indicar el inicio y derecha para indicar el fin
print(mascotas[2:])
print(mascotas[-1])  # ultimo elemento

# acceder a los elementos pares
print(mascotas[::2])
# devuelve Pelusa y Copito porque empieza a contar desde Pelusa y salta de 2 en 2
print(mascotas[1::2])

numeros = list(range(21))
print(numeros[::2])  # pares
print(numeros[1::2])  # impares

numerosImpares = list(range(1, 21))
print(numerosImpares[::2])  # impares
