# Returns the Fibonacci sequence with 'maximo' members
def fibo(maximo):
    a, b = 0, 1
    output = []
    iteration = 0
    while iteration <= maximo:
        output.append(a)
        a, b = b, b + a
        iteration += 1
    return output


# Returns the nth number of a Fibonacci sequence

def recursiveNfibo(n):
    if n <= 1:
        return n
    else:
        return (recursiveNfibo(n - 1) + recursiveNfibo(n - 2))


print(fibo(10))
print(recursiveNfibo(4))
