usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# nombres = []

# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)


# [expresion for item in iterable] -> se conoce como map
nombres = [usuario[0] for usuario in usuarios]
print(nombres)

# devolver elemento entero
nombres = [usuario for usuario in usuarios]
print(nombres)

# filtar -> se conoce como filter
nombres = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres)

# filtrar y trasnformar -> se conoce como map y filter
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)


# Usar las funciones de filter y map para hacer lo mismo de antes pero con las listas de comprension
# muchos desarrolladores prefieren usar las funciones de map y filter. Esta bien de ambas maneras
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
