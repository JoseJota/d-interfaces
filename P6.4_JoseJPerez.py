def item_order(orden):
	a = orden.count("ensalada")
	b = orden.count("hamburguesa")
	c = orden.count("agua")
	return "ensalada: " + str(a) + " hamburguesa: " + str(b) + " agua: " + str(c)
