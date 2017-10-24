n = input("Dígame cuántas palabras tiene la lista: ")
lista = list()
if (int(n) <= 0):
    print("¡Imposible!")
else:
    for i in range(int(n)):
        palabra = input("Dígame la palabra " + str(i + 1) + ": ")
        lista.append(palabra)
    print("La lista creada es:", lista)

    print("La lista ordenada es:", sorted(lista))