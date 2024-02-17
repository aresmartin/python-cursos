"""
Un formateador de números de teléfono básicamente agrupa los dígitos en grupos de tres
e ignora cualquier carácter que no sea un dígito. Por ejemplo, (988)387001 se convertiría en 988 387 001. 
Además, el número puede estar precedido o no por el código de páis (dos dígitos), mediante el formato ‘+’ o ‘00’: 
+34(988) 387001 o 0034 (988) 387001 deben convertirse en +34 988 387 001.
Finalmente, pueden encontrarse letras de la a a la z en el número, que deben
traducirse a dígitos siguiendo la convención:
2: a, b, c; 3: d, e, f; 4: g, h, i; 5: j, k, l; 6: m, n, o; 7: p, q, r, s; 8: t, u, v; y 9: w, y, z.
Así, 900 ESI NFO sería 900 374 636.
"""


def formatear_numero(numero):

    if numero[0:3] == "+34":
        prefijo = numero[:3]
        numero = numero[3:]
        numero = letras_a_numeros(numero)
        numero = quitar_caracteres(numero)
        numero = grupos_tres_prefijo(prefijo, numero)
        print(numero)
    elif numero[0:2] == "00":
        prefijo = numero[:2]
        numero = numero[2:]
        numero = letras_a_numeros(numero)
        numero = quitar_caracteres(numero)
        numero = grupos_tres_prefijo(prefijo, numero)
        print(numero)

    else:
        numero = letras_a_numeros(numero)
        numero = quitar_caracteres(numero)
        numero = grupos_tres(numero)
        print(numero)


def grupos_tres(numero):
    # separar el numero en grupos de 3
    numero = str(numero)[:3] + " " + str(numero)[3:6] + \
        " " + str(numero)[6:9] + " " + str(numero)[9:]
    return numero


def quitar_caracteres(numero):
    # quitar caracteres no deseados (solo numeros)
    numero = ''.join(filter(str.isdigit, numero))
    return numero


def grupos_tres_prefijo(prefijo, numero):
    # separar el numero en grupos de 3
    if prefijo[0:3] == "+34":
        numero = str(prefijo)[:3] + " " + str(numero)[:3] + \
            " " + str(numero)[3:6] + " " + \
            str(numero)[6:9] + " " + str(numero)[9:]
        # numero = prefijo + " " + numero
    elif prefijo[0:2] == "00":
        numero = str(prefijo)[:2] + " " + str(numero)[:3] + \
            " " + str(numero)[3:6] + " " + \
            str(numero)[6:9] + " " + str(numero)[9:]
        # numero = prefijo[0:2] + " " + numero
    return numero


def letras_a_numeros(numero):
    mapeo = {'a': '2', 'b': '2', 'c': '2',
             'd': '3', 'e': '3', 'f': '3',
             'g': '4', 'h': '4', 'i': '4',
             'j': '5', 'k': '5', 'l': '5',
             'm': '6', 'n': '6', 'o': '6',
             'p': '7', 'q': '7', 'r': '7', 's': '7',
             't': '8', 'u': '8', 'v': '8',
             'w': '9', 'x': '9', 'y': '9', 'z': '9'}
    traduccion = ""
    numero = numero.lower()
    for char in numero:
        if char.isalpha():
            traduccion += mapeo[char]
        else:
            traduccion += char
    return traduccion


formatear_numero("988387001")  # 988 387 001
formatear_numero("(988)387001")  # 988 387 001
formatear_numero("+34988387001")
formatear_numero("00988387001")
formatear_numero("+34(988)387001")
formatear_numero("900ESINFO")
formatear_numero("900(ESI)NFO")
formatear_numero("+34900(ESI)NFO")
formatear_numero("00900(ESI)NFO")
