def isVowel2(char):
	voc = ["a", "e", "i", "o", "u"]
	for i in voc:
		if (char.lower() == i):
			return True
	return False		