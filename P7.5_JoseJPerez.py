n = input("Dígame cuántas palabras tiene la lista: ")
lista = list()
if (int(n) <= 0):
    print("¡Imposible!")
else:
    for i in range(int(n)):
        palabra = input("Dígame la palabra " + str(i+1) + ": ")
        lista.append(palabra)
    print("La lista creada es:", lista)

    n = input("Dígame cuántas palabras tiene la lista de palabras a eliminar: ")
    lista2 = list()
    if (int(n) <= 0):
        print("¡Imposible!")
    else:
           for i in lista2:
               while i in lista:
                   lista.remove(i)