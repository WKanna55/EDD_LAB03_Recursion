#Ejercicio N°2: Suma de los primeros n numeros naturales

#Complejidad de tiempo (n)
#Complejidad de espacio(n)
numero = 10
def sumaConsecutiva(n):
    if n == 1: return 1 #caso base
    return n + sumaConsecutiva(n - 1) # llamada recursiva

print(sumaConsecutiva(numero))
