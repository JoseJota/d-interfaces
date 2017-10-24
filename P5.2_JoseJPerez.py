def isVowel(char):
	voc = ["a", "e", "i", "o", "u"]
	i = 0
	while (i < (len(voc)-1)):
		if (char.lower() == voc[i]):
			return True
		i += 1	
	return False