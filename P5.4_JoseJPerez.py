def isVowel2(char):
	voc = ["a", "e", "i", "o", "u"]
	for i in voc:
		if (char.lower() == i):
			return True
	return False

s = input("Introduce una cadena:")
nV = 0
#Llamo al método de forma recursiva y cuento el número de veces que devuelve True.
for i in s:
	if(isVowel2(i)):
		nV += 1
print("Número de vocales en la cadena: ", nV) 
