buscar = 10
for numero in range(5):  # range(5) es un iterable de 0 a 4
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:  # else del for
    print("no encontrado", buscar)

# Ireracion de strings
for char in "Ultimate python":
    print(char)
