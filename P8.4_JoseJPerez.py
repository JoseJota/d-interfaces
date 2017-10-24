a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
u0 = float(input("Valor de U(0): "))
n = int(input("¿Cuántos términos quiere? "))
sucesion = list()

sucesion.append(u0)

for i in range(n - 1):
    sucesion.append(a * (sucesion[i]) + b)

print("Resultado:", sucesion)