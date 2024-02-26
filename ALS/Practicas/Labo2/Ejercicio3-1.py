def evalua_expresion(expresion):
    # Divide la expresión en tokens utilizando espacios como delimitadores
    tokens = expresion.split()

    # Función recursiva para evaluar la expresión
    def evalua_recursivo(tokens):
        if not tokens:
            raise ValueError("Expresión vacía")

        token = tokens.pop(0)  # Obtiene el primer token

        if token.isdigit():  # Si es un operando, devuelve su valor
            return int(token)
        elif token in "+-*/":  # Si es un operador, evalúa la subexpresión
            op2 = evalua_recursivo(tokens)
            op1 = evalua_recursivo(tokens)

            if token == "+":
                return op1 + op2
            elif token == "-":
                return op1 - op2
            elif token == "*":
                return op1 * op2
            elif token == "/":
                return op1 / op2
        else:
            raise ValueError(f"Token no válido: {token}")

    try:
        resultado = evalua_recursivo(tokens)
        return resultado
    except Exception as e:
        return f"Error: {str(e)}"


# Ejemplos de uso
expresion1 = "+ 1 2"
expresion2 = "+ 1 - 5 * 2 4"
expresion3 = "+ + 3 4 * 2 5"

print(f"Resultado 1: {evalua_expresion(expresion1)}")
print(f"Resultado 2: {evalua_expresion(expresion2)}")
print(f"Resultado 3: {evalua_expresion(expresion3)}")
