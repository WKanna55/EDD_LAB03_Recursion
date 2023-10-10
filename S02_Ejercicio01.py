#Ejercicio n°1: factorial de n

#Complejidad de tiempo (n)
#Complejidad de espacio(n)
numero = 4
def factorial(n):
    if n == 1: return 1 #Caso base
    return n * factorial(n - 1) #Llamada Recursiva

print(factorial(numero))
