bin = input('Número binario:')
dec = 0
for i, c in enumerate(bin):
	if (c == "1"):
		dec += 2**(len(bin)-i-1)
print(dec)
