class Coche:
	def __init__(self, gasolina): #constructor
		self.gasolina = gasolina
		print("Tenemos", gasolina, "litros")
	def arrancar(self):        #método
		if self.gasolina > 0:
			print("Arranca")
		else:
			print("No arranca")
	def conducir(self): #método
		if self.gasolina > 0:
			self.gasolina -= 1
			print("Quedan", self.gasolina, "litros")
		else:
			print("No se mueve")
			mi_coche.arrancar()