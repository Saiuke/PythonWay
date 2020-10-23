def findPrime(maxNum):
    for n in range(2, maxNum):
        for x in range(2, n):
            if n % x == 0:
                print(n, ' equals to ', x, ' * ', n // x)
                break
        else:
            print(n, ' is a prime number')


def printOnlyPrimes(maxNum):
    foundPrimes = []
    for n in range(2, maxNum):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            foundPrimes.append(n)
    return foundPrimes


findPrime(20)
# print(printOnlyPrimes(50000))
