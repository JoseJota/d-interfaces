def problema1(varA, varB):
	if (isinstance(varA, str) | isinstance(varB, str)):
		print("Cadena")
	elif (varA > varB):
		print("Grande")
	elif (varA == varB):
		print("Igual")
	else:
		print("Más pequeño")