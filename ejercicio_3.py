import random

#Definición de la función

def Sumalista(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma
    
#input
#creamos lista vacia

lista = []

#Tamaño de la lista

n = int(input("Dijite el tamaño de la lista: "))

for i in range(n):
    num = random.randint(1,9)
    lista.append(num)


#processing

print(f"lista: {lista}")
print(f"la suma es {Sumalista(lista)}")