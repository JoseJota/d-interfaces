n = input("Dígame cuántas palabras tiene la lista: ")
lista = list()
if (int(n) <= 0):
    print("¡Imposible!")
else:
    for i in range(int(n)):
        palabra = input("Dígame la palabra " + str(i+1) + ": ")
        lista.append(palabra)
    print("La lista creada es:", lista)

    lista2 = []
    for i in lista:
        if i in lista2:
            continue
        lista2.append(i)
    print("La lista sin repeticiones es:", lista2)
