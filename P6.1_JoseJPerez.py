def iterPower(base, exp):
	if (exp < 0):
		return None
	if (exp == 0):
		return 1
	result = base
	for i in range(exp-1):
		result *= base
	return result
print (iterPower(5,2))