import random

#Definir función

def calcular_promedio(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    promedio = suma / len(lista)
    return promedio


#input
#creamos lista vacia

lista = []

#Tamaño de la lista

n = int(input("Dijite el tamaño de la lista: "))

for i in range(n):
    num = random.randint(14,18)
    lista.append(num)

#processing

print(f"lista: {lista}")
print(f"el promedio de la lista es {calcular_promedio(lista)}")