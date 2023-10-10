#Ejercicio N°5: Suma de digitos de un numero

#Complejidad de tiempo o(n)
#Complejidad de espacio o(n)

def sumaDigitosRec(n, i, sum):
    if i == len(n): return sum #caso base
    sum += int(n[i])
    return sumaDigitosRec(n, i+1,sum) # llamada recursiva

print(sumaDigitosRec("125", 0, 0))