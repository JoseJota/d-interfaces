n = input("Dígame cuántas palabras tiene la lista: ")
lista = list()
if (int(n) <= 0):
    print("¡Imposible!")
else:
    for i in range(int(n)):
        palabra = input("Dígame la palabra " + str(i+1) + ": ")
        lista.append(palabra)
    print("La lista creada es: ", lista)
    palabraBuscada = input("Dígame la palabra a buscar: ")
    resultado = lista.count(palabraBuscada)
    if (resultado == 0):
        print("La palabra '", palabraBuscada, "' no aparece en la lista." )
    elif (resultado == 1):
        print("La palabra '", palabraBuscada, "' aparece 1 vez en la lista.")
    else:
        print("La palabra '", palabraBuscada, "' aparece ", resultado, " veces en la lista." )