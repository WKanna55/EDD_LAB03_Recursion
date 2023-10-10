#Ejercicio N°7: Suma de elementos en una lista

#Complejidad de tiempo o(n)
#Complejidad de espacio o(n)
list = [1, 2, 3, 4, 5]
def sumListNum(lista, indice):
    if indice == len(lista): return 0 #Caso base
    return lista[indice] + sumListNum(lista, indice+1) #llamada recursiva

print(sumListNum(list, 0))
