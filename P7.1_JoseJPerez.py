#Se guarda el valor de cuántas palabras tiene la lista.
n = input("Dígame cuántas palabras tiene la lista: ")
lista = list()

#La lista no puede tener 0 o menos palabras
if (int(n) <= 0):
    print("¡Imposible!")
else:
    for i in range(int(n)):
    	#Se añaden palabras hasta llegar al número de palabras
        palabra = input("Dígame la palabra " + str(i+1) + ": ")
        lista.append(palabra)
    print("Resultado:", lista)

