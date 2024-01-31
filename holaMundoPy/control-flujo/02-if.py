# Evaluaciones de arriba hacia abajo. si pongo edad > 24 en elif, no se ejecuta porque ya se ejecutó la condición de edad > 17
# Siempre se ejecuta el primer if que se cumpla, no se ejecutan los demás aunque se cumplan

edad = 70
if edad > 65:
    print("Puede ver la película con super descuento")
elif edad > 54:
    print("Puede ver la película con descuento")
elif edad > 17:
    print("Puede ver la película")
# else:
    # print("No puede ver la película")
    # print("Ve a otro lado")


print("Listo")
