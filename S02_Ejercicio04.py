#Ejercicio N°4: Potencia recursiva

#Complejidad de tiempo o(n)
#complejidad de espacio o(n)
def potenciaRecursiva(x, n):
    if n == 1:return x #caso base
    return x * potenciaRecursiva(x, n-1) #llamada recursiva

print(potenciaRecursiva(3, 3))
