"""
Escribe una función es_anagrama(s1, s2) que determine si son anagramas 
dos cadenas pasadas como argumento. Dos cadenas son anagramas la una de la otra, 
si tienen las mismas letras pero en distinto orden.
"""
lista_s1 = []
lista_s2 = []


def es_anagrama(s1, s2):
    for char in s1:
        lista_s1.append(char)

    for char2 in s2:
        lista_s2.append(char2)

    print(lista_s1)
    print(lista_s2)

    lista_s1.sort()
    lista_s2.sort()

    print(lista_s1)
    print(lista_s2)

    if lista_s1 == lista_s2:
        print("SON ANAGRAMAS")
    else:
        print("NO son anagramas")
    lista_s2.clear()
    lista_s1.clear()


es_anagrama("pablo", "hola")
es_anagrama("sergio", "riesgo")
es_anagrama("delira", "lidera")
