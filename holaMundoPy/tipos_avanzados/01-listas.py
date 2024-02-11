numeros = [1, 2, 3]
letras = ["a", "b", "c"]
matriz = [[1, 2, 3], [4, 5, 6]]
print(matriz)

ceros = [0] * 10  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] es lo mismo
cerosyunos = [0, 1] * 10
print(ceros)
print(cerosyunos)

# juntar listas
alfanumerico = numeros + letras
print(alfanumerico)

# crear listado con rango de numeros
# crear una lista de 0 a 10-> haciendo range(1,11) empieza en 1 y termina en 10 (no incluye el 11)
rango = list(range(1, 11))
print(rango)

# los strings son listas de caracteres iterables (se pueden recorrer)
chars = list("Hola Mundo")
print(chars)
