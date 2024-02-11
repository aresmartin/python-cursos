# una tupla es lo mismo que una lista, con la diferencia que no se puede modificar, ni añadir ni eleminar elementos
# puedes crear nuevas tuplas pero no modificar las existentes

numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

# transformar lista a tupla
punto = tuple([1, 2])
print(punto)

# append y pop no funcionan en tuplas
menosNumeros = numeros[:2]
print("Menos numeros", menosNumeros)

# desempaquetar tuplas
primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)

# numeros[0] = 5 _-> Nooorl

# En el caso de modificar una tupla, se debe convertir a lista, modificar y luego convertir a tupla (NO RECOMENDADO)
listaNumeros = list(numeros)
listaNumeros[0] = "Nitram Sera"
print(listaNumeros)
