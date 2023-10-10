#Ejercicio N°3: Fibonacci recursivo

#complejidad de tiempo(2^n)
#complejidad de espacio(n)
def fibonacciRecursivo(n):
    if n == 0: return 0 #Caso base
    if n == 1: return 1 #Caso base
    return fibonacciRecursivo(n-1)+fibonacciRecursivo(n-2) # Llamada recursiva

print(fibonacciRecursivo(15))
