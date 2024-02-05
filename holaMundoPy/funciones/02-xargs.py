def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    # identacion para que no se ejecute en cada iteracion si no al final
    print(resultado)


suma(2, 5, 7)
suma(2, 5)
suma(2, 4, 5, 7, 88, 54)
