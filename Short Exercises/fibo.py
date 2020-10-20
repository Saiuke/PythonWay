def fibo(max):
    a, b = 0, 1
    output = []
    exec = 0
    while exec <= max:
        output.append(a)
        a, b = b, b+a
        exec += 1
    return output

print(fibo(1000))
