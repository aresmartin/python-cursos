lista1 = [1, 2, 3, 4]
# print(lista)
# print(*lista)  # desempaquetar lista

# tambien se puede hacer con tuplas
# tupla = (1, 2, 3, 4)
# print(*tupla)

lista2 = [5, 6]

combinada = ["Hola", *lista1, "mundo", *lista2, "Chanchito"]
print(combinada)

# diccionarios

punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15}

# se asgina de derecha a izquierda y si hay claves repetidas se toma el valor de la derecha
nuevoPunto = {**punto1, "lala": "hola mundo", **punto2, "z": "mundo"}
print(nuevoPunto)
