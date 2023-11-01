lista = []
lista2 = []

for i in range(0,10):
    lista.append(i)
    
for j in range(0,4):
    lista2.append(j)
    
print(lista)
print(lista2)

def nigger():
    for i in lista.copy():
        print(lista)
        print("in first for loop")
        for j in lista2.copy():
            print("in second for loop")
            if i <= 0:
                print("entered if")
                lista.remove(i)
                break
            indice1 = lista.index(i)
            indice2 = lista2.index(j)
            lista[indice1] -= lista2[indice2]
            print(lista[indice1])

# for i in lista:
#     cuerda = str(i)
#     if i:
#         print(f"true " + cuerda)
#     else:
#         print(f"false " + cuerda)
nigger()
print(lista)
print(lista2)
