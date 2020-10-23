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

def recursiveFibo(n):
    if n <= 1:
        return n
    else:
        return (recursiveFibo(n - 1) + recursiveFibo(n - 2))


def calcFibo(n):
    sequence = [0, 1]
    iteration = 0
    while iteration <= n - 2: # The sequence already starts with 2 members
        sequence[0], sequence[1] = sequence[1], sequence[0] + sequence[1]
        iteration += 1
    return sequence[1]

print(fibo(18))
print(recursiveFibo(4))
print(calcFibo(18))
