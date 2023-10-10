#Ejercicio n°1: factorial de n

#Complejidad de tiempo (n)
#Complejidad de espacio(n)
numero = 4
def factorial(n):
    if n == 1: return 1 #Caso base
    return n * factorial(n - 1) #Llamada Recursiva

print(factorial(numero))

#===================================================================================

#Ejercicio N°2: Suma de los primeros n numeros naturales

#Complejidad de tiempo (n)
#Complejidad de espacio(n)
numero = 10
def sumaConsecutiva(n):
    if n == 1: return 1 #caso base
    return n + sumaConsecutiva(n - 1) # llamada recursiva

print(sumaConsecutiva(numero))

#===================================================================================

#Ejercicio N°3: Fibonacci recursivo

#complejidad de tiempo(2^n)
#complejidad de espacio(n)
def fibonacciRecursivo(n):
    if n == 0: return 0 #Caso base
    if n == 1: return 1 #Caso base
    return fibonacciRecursivo(n-1)+fibonacciRecursivo(n-2) # Llamada recursiva

print(fibonacciRecursivo(15))

#===================================================================================

#Ejercicio N°4: Potencia recursiva

#Complejidad de tiempo o(n)
#complejidad de espacio o(n)
def potenciaRecursiva(x, n):
    if n == 1:return x #caso base
    return x * potenciaRecursiva(x, n-1) #llamada recursiva

print(potenciaRecursiva(3, 3))

#===================================================================================

#Ejercicio N°5: Suma de digitos de un numero

#Complejidad de tiempo o(n)
#Complejidad de espacio o(n)

def sumaDigitosRec(n, i, sum):
    if i == len(n): return sum #caso base
    sum += int(n[i])
    return sumaDigitosRec(n, i+1,sum) # llamada recursiva

print(sumaDigitosRec("125", 0, 0))

#===================================================================================

#Ejercicio N°6: Conteo de caracteres

#Complejidad de tiempo o(n)
#Complejidad de espacio o(n)

def conteoCaracter(cadena, caracter, indice, contador):
    if indice == len(cadena): return contador #Caso base
    if cadena[indice] == caracter: contador +=1
    return conteoCaracter(cadena,caracter,indice + 1, contador) # llamada recursiva

print(conteoCaracter("kannaa", 'a', 0, 0))

#===================================================================================

#Ejercicio N°7: Suma de elementos en una lista

#Complejidad de tiempo o(n)
#Complejidad de espacio o(n)
list = [1, 2, 3, 4, 5]
def sumListNum(lista, indice):
    if indice == len(lista): return 0 #Caso base
    return lista[indice] + sumListNum(lista, indice+1) #llamada recursiva

print(sumListNum(list, 0))

