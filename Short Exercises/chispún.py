def chispun():
    n = int(input("Inserte el valor de N:"))
    dig = int(input("Inserte el valor de Dig:"))

    for key in range(1, n + 1):
        if dig != 0:
            if key % dig == 0:
                print("*")
            else:
                print(key)
        else:
            # Si dig es igual a cero imprime secuecia
            print(key)


chispun()
