"""
El programa aceptará una expresión numérica del usuario, la evaluará y 
devolverá el resultado. La cadena utilizará el formato prefijo, con lo 
que no serán necesarios los paréntesis. Un ejemplo podría ser: + 1 2. 
Otro, más complejo, + 1 - 5 * 2 4, que se evalúa de izquierda a derecha como:
 sumarle a uno el resultado de restarle a cinco el producto de 2 por 4. Será 
 obligatorio utilizar espacios como delimitadores entre signos y valores numéricos.
   Todas las operaciones soportadas emplearán dos operandos.
Este ejercicio es muy sencillo si se utilizar el método split() de las cadenas, 
que ya por defecto toma los espacios como separadores. Será necesario crear una 
función recursiva que, recorriendo la lista obtenida de izquierda a derecha, 
calcule el resultado. Nótese que cada vez que encuentre un signo, deberá retroceder
 y llamarse a sí misma para calcular la subexpresión.
¿Puedes hacerlo permitiendo expresiones prefijas y postfijas? Es decir, 
el programa ante 1 3 4 + + sabe que está ante una expresión postfija y que debe 
empezar por el final y retroceder, en lugar de avanzar (nota: en las expresiones
 prefijas siempre hay un signo al principio, mientras que en las postfijas siempre 
 hay uno al final).
"""


def evaluar_expresion(expresion):
    # Dividir la expresión en tokens (números y operadores)
    tokens = expresion.split()

    # Pila para almacenar los valores
    stack = []

    # Función recursiva para evaluar la expresión
    def evaluar_recursivo():
        if not tokens:
            return None

        token_actual = tokens.pop()

        # Si el token es un operador, calcular la subexpresión
        if token_actual in {'+', '-', '*', '/'}:
            operand2 = evaluar_recursivo()
            operand1 = evaluar_recursivo()

            # Realizar la operación correspondiente
            if token_actual == '+':
                return operand1 + operand2
            elif token_actual == '-':
                return operand1 - operand2
            elif token_actual == '*':
                return operand1 * operand2
            elif token_actual == '/':
                return operand1 / operand2

        # Si el token es un número, simplemente devolverlo
        else:
            return float(token_actual)

    # Llamar a la función recursiva para obtener el resultado final
    resultado = evaluar_recursivo()

    return resultado


# Ejemplos de uso
expresion_prefija = "+ 1 - 5 * 2 4"
expresion_postfija = "1 3 4 + +"

resultado_prefijo = evaluar_expresion(expresion_prefija)
resultado_postfijo = evaluar_expresion(expresion_postfija)

print(f"Resultado Expresión Prefija: {resultado_prefijo}")
print(f"Resultado Expresión Postfija: {resultado_postfijo}")
