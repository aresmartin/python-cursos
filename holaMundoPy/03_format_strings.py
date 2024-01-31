nombre = "Nicolas"
apellido = "Shurman"
nombre_completo = f"{nombre[0]} {2+5}"
print(nombre_completo)

animal = "   chanCHito feliz   "
# realizar un strip antes de un capitalize para mejor funcionamiento
print(animal.strip().capitalize())  # concatenar métodos
print(animal.title())
print(animal.strip())  # Elimina espacios en blanco
print(animal.lstrip())  # Elimina espacios en blanco a la izquierda
print(animal.rstrip())  # Elimina espacios en blanco a la derecha
print(animal.find("cH"))  # devuelve el indice de la primera ocurrencia
print(animal.strip().replace("feliz", "triste"))
print("nCH" in animal)  # devuelve un boolean si existe o no
print("nCH" not in animal)
