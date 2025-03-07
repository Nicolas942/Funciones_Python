print("--------------------------------")
print(" BUSCAR UN NÚMEOR EN CONJUNTO"   )
print("--------------------------------")

# Definir la función

def BuscarDatoEnLista(datoABuscar, lista):
    r = False
    for i in lista:
        if i == datoABuscar:
            r = True
    return r

# input

dato = int(input("Número a buscar: "))

lista = [1,2,3,4,5]

# processing

if BuscarDatoEnLista(dato, lista):
    print("Lo encontré")
else:
    print("No lo encontré")

# output

print("\nEso era...")