def divisores(x):
    listaDivisores = list()
    for i in range(1, int(x**.5) + 1):
        if (x % i == 0):
            listaDivisores.append(i)
            listaDivisores.append(int(x / i))

    return listaDivisores

x = int(input("Dígame un número: "))

if (x <= 1):
    print("Primos hasta el número", x)
else:
    print("Primos hasta el número", x, ":", [i for i in range(2, x) if ((len(divisores(i)) == 2))])
