mascotas = [
    "Wolfgang",
    "Pelusa",
    "Pulga",
    "Felipe",
    "Pulga",
    "Chanchito feliz"
]
mascotas.insert(1, "Melvin")
mascotas.append("Chanchito triste")  # agregar al final

mascotas.remove("Pulga")  # elimina la primera coincidencia
print(mascotas)
mascotas.pop()  # elimina el ultimo elemento
print(mascotas)
mascotas.pop(1)  # elimina el elemento en la posicion 1
print(mascotas)
del mascotas[0]  # elimina el elemento en la posicion 0
print(mascotas)
mascotas.clear()  # elimina todos los elementos
print(mascotas)
