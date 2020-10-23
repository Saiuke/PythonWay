def fibo(maximo):
    a, b = 0, 1
    output = []
    iteration = 0
    while iteration <= maximo:
        output.append(a)
        a, b = b, b + a
        iteration += 1
    return output


print(fibo(1000))
