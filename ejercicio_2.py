def Nombre(cadena, veces):
    for i in range(1,veces + 1):
        print(f"{i}. {cadena}")

cadena= input("Ingrese una cadena de texto: ")
veces = int(input("Cuantas veces quiere repetir el texto: "))

print(Nombre(cadena, veces))

print("Eso era ...")