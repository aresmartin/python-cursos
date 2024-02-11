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

    if numero[:3] == "+34" or numero[:2] == "00":
        prefijo = "+34"
        grupos_tres_prefijo(prefijo, numero)
        print(numero)
    else:
        grupos_tres(numero)
        quitar_caracteres(numero)

        print(numero)


def quitar_caracteres(numero):
    # quitar caracteres no deseados (solo numeros)
    numero = ''.join(filter(str.isdigit, numero))


def grupos_tres(numero):
    # separar el numero en grupos de 3
    numero = str(numero)[:3] + " " + str(numero)[3:6] + \
        " " + str(numero)[6:9] + " " + str(numero)[9:]


def grupos_tres_prefijo(prefijo, numero):
    # separar el numero en grupos de 3
    numero = str(prefijo)[:3] + " " + str(numero)[3:6] + \
        " " + str(numero)[6:9] + " " + str(numero)[9:]


formatear_numero("988387001")  # 988 387 001
formatear_numero("(988)387001")  # 988 387 001
formatear_numero("+34988387001")
