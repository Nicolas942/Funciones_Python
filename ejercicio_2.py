def Nombre(nombre, veces):
    for i in range(1,veces +1):
        print(f"{i}. {nombre}")

nombre = input("Ingrese su nombre ")
veces = int(input("Cuantas veces quiere repetir el texto: "))

print(Nombre(nombre, veces))