print("Bienvenido a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, multi, div y resta")

# suma = n1 + n2
# resta = n1 - n2
# multi = n1 * n2
# div = n1 / n2

resultado = ""


while True:
    if not resultado:
        resultado = input("Ingrese un número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)  # si no es salir, lo convierto a int
    op = input("Ingrese la operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingrese siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operación no válida")
        break
    print(f"El resultado es {resultado}")
