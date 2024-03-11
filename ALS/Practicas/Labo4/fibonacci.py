"""
Crea la funcion fibonacci utilizando programación dinámica
"""

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

if __name__ == "__main__":
    n = 10
    resultado = fibonacci(n)
    print(f"El término {n} de la secuencia de Fibonacci es: {resultado}")