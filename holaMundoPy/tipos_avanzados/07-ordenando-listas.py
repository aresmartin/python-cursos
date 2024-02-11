numeros = [2, 4, 1, 45, 75, 22]

numeros.sort()  # ordenar lista
print(numeros)

# numeros.sort(reverse=True)  # ordenar lista de forma inversa
# sorted() no modifica la lista original -> devuelve una nueva lista
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

# ordenar algo más complejo
usuarios = [[4, "Chanchito"], [3, "Felipe"], [2, "Ricardo"], [1, "Carlos"]]
usuarios.sort()  # ordena por el primer elemento de la lista
print(usuarios)

usuarios2 = [["Chanchito", 4], ["Felipe", 3], ["Ricardo", 2], ["Carlos", 1]]

# funcion lambda para ordenar por el segundo elemento de la lista
usuarios2.sort(key=lambda el: el[1], reverse=True)
print(usuarios2)
