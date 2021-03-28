def findHappyNumber(numInicial: int, nuevoNumero = None):
    nuevoNumero = numInicial if nuevoNumero is None else nuevoNumero
    if nuevoNumero == 4:
        print("El número " + str(numInicial) + " no es feliz.")
    elif nuevoNumero == 1:
        print("El número " + str(numInicial) + " es feliz.")
    else:
        # Divide el número en una lista
        listaNum = [int(d) for d in str(nuevoNumero)]
        # Suma el cuadrado de todos los elementos de la lista
        nuevoNumero = sum([i * i for i in listaNum])
        findHappyNumber(numInicial, nuevoNumero)


testCase = [200503, 1456352, 3, 7, 13, 4, 3445]

for number in testCase:
    findHappyNumber(number)
