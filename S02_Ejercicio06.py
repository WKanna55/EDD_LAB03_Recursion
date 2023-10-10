#Ejercicio N°6: Conteo de caracteres

#Complejidad de tiempo o(n)
#Complejidad de espacio o(n)

def conteoCaracter(cadena, caracter, indice, contador):
    if indice == len(cadena): return contador #Caso base
    if cadena[indice] == caracter: contador +=1
    return conteoCaracter(cadena,caracter,indice + 1, contador) # llamada recursiva

print(conteoCaracter("kannaa", 'a', 0, 0))
