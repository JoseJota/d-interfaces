def eliminarElementosRepetidos(lista):
    listaSinRepeticiones = []
    
    for i in lista:
        if i not in listaSinRepeticiones:
            listaSinRepeticiones.append(i)
    return listaSinRepeticiones

x = int(input("Dígame un número: "))

listaDivisores = list()

for i in range(1, int(x**.5) + 1):
    if (x % i == 0):
        listaDivisores.append(i)
        listaDivisores.append(int(x / i))
listaDivisores = eliminarElementosRepetidos(listaDivisores)
listaDivisores = sorted(listaDivisores)

print(x, "tiene", len(listaDivisores), "divisores:", listaDivisores)