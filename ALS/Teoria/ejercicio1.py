"""
Ejercicio 1 -> crear programa que calcule los primeros 100 números fibonacci
"""

a = 0
b = 1
resultado = 0

while resultado < 100:
    print(resultado)
    resultado = a + b
    a = b
    b = resultado
