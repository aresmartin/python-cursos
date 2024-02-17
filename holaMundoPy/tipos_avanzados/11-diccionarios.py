punto = {"x": 25, "y": 50}  # diccionario con llaves y valores (key-value)
print(punto)

print(punto["x"])  # acceder a un valor por su llave
print(punto["y"])

punto["z"] = 45  # agregar un nuevo valor
# print(punto, punto["lala"])

if "lala" in punto:
    print("encontre lala", punto["lala"])

print(punto.get("lala", 97))

del punto["x"]  # eliminar un valor
del (punto["y"])  # eliminar un valor
print(punto)

punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

# otra sintaxis mejor
for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

# uso más realista de los diccionarios
usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"},

]

# iterar los nombres
for usuario in usuarios:
    print(usuario["nombre"])
