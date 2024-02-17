# set significa grupo, conjunto, colección
# Un set es una colección de datos que no se puede repetir y no está ordenada
primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)
print(segundo)
# print(primer)

# primer.add(5)
# primer.remove(1)
# print(primer)


print(primer | segundo)  # union
print(primer & segundo)  # intersección
print(primer - segundo)  # diferencia
# diferencia simétrica (elementos que no se repiten en ambos sets)
print(primer ^ segundo)

if 5 in segundo:
    print("Hola mundo")
