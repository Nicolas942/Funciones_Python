print("--------------------------------")
print(" BUSCAR UN NÚMEOR EN CONJUNTO"   )
print("--------------------------------")

# entrada

b = int(input("Número a buscar: "))

#processing

a = [1,2,3,4,5]

r = False

for i in a:
    if i == b:
        print("Lo encontre")
        r = True
    if r == False:
        print("No lo encontre")

#output

print("\nEso era...")