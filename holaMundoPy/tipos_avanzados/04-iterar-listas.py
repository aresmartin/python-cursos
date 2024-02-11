mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito feliz"]

for mascota in enumerate(mascotas):
    print(mascota)  # devuelve una tupla con el indice y el valor

# acceder a los indices de una lista
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
