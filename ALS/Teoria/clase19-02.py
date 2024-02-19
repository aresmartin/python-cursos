nombre = "ALS"
nombre = "D" + nombre[1] + nombre[2]
print(nombre)

nombre = nombre[0] + "I" + "A"
print(nombre)

nombre = "I" + nombre[1:]

# LISTAS
l = [11, 22, 33, 44, 55, 66, 77, 88, 99]
print(l[1::2])  # numeros pares

# la parte central de la lista sea otro valor
l[3:6] = [4, 5, 6]
print(l)

# Tuplas: son inmutables
t0 = ()
t1 = (1,)  # las tuplas de 1 elemento deben llevar una coma
t2 = (1, 2)

# Matrices (mas o menos)
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(m)

print(m[0])
print(m[1])
print(m[2])

print(len(m))

print(len(m[0]) + len(m[1]) + len(m[2]))  # capacidad total de la matriz

# mejor con bucle for
for i in range(len(m)):  # range crea una lista de numeros
    print(m[i])

for fila in m:
    print(fila)

tam = 0
for fila in m:
    tam += len(fila)
print(tam)

# Diccionarios
decenas = {
    10: "diez",
    20: "veinte",
    30: "treinta",
    40: "cuarenta",
    50: "cincuenta",
    60: "sesenta",
    70: "setenta",
    80: "ochenta",
    90: "noventa"
}

print(decenas[20])
print(list(decenas.keys()))  # devuelve una lista con las claves
print(list(decenas.values()))  # devuelve una lista con los valores

# Para buscar elementos mejor usar:
valor_ciento_cuarenta = decenas.get("Ciento cuarenta")

if valor_ciento_cuarenta is None:
    print("No existe")
else:
    print("Ciento cuarenta: ", valor_ciento_cuarenta)
print(valor_ciento_cuarenta)

valor_ciento_cuarenta is None
