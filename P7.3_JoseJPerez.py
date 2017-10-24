
n = input("Dígame cuántas palabras tiene la lista: ")
lista = list()
if (int(n) <= 0):
    print("¡Imposible!")
else:
    for i in range(int(n)):
        palabra = input("Dígame la palabra " + str(i+1) + ": ")
        lista.append(palabra)
    print("La lista creada es:", lista)
    #¿No tenemos en cuenta si las palabras a intercambiar están o no en la lista?
    cambio1 = input("Sustituir la palabra: ")
    cambio2 = input("por la palabra: ")

    for i, palabra in enumerate(lista):
        if (palabra == cambio1):
            lista[i] = cambio2
    print("La lista es ahora:", lista)