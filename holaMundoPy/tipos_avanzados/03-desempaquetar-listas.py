numeros = [1, 2, 3]

# # feo!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# print(primero, segundo, tercero)

# primero, segundo, tercero = numeros
# print(primero, segundo, tercero)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, *otros, ultimo = numeros  # *otros es una lista
print(primero, ultimo, otros)
