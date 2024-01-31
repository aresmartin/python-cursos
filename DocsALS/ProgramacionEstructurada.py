with open('./salida.txt', 'rt') as f:
    lineas = f.readlines()
    for linea in lineas:
        print(linea)