n = input("Dígame cuántas palabras tiene la lista: ")
lista = list()
if (int(n) <= 0):
    print("¡Imposible!")
else:
    for i in range(int(n)):
        palabra = input("Dígame la palabra " + str(i+1) + ": ")
        lista.append(palabra)
    print("La lista creada es:", lista)
    #¿No tenemos en cuenta si la palabra aparece más de una vez en la lista, o incluso ninguna?
    eliminar = input("Palabra a eliminar: ")
    lista.remove(eliminar)
    print("La lista es ahora:", lista)
