# Returns the GDC of 2 two integers
def findGCD(a, b):
    minNumber = a if a < b else b
    minNumber = minNumber if minNumber > 0 else minNumber * -1  # Ensures that minNumber is always positive, like you
    commonDivisors = [x for x in range(2, minNumber + 1) if (a % x == 0) and (b % x == 0)]
    return max(commonDivisors) if len(commonDivisors) >= 1 else 1
    # To get the MDC would suffice to substitute the max function to min


print(findGCD(18, 81))
print(findGCD(12, 4))
print(findGCD(1024, 512))
print(findGCD(15, 2))
print(findGCD(-18, 9))


#################################################################################################################

def calcFactorial(n):
    if n <= 1:
        return 1
    else:
        return n * calcFactorial(n - 1)


print('Factorial de 17: ', calcFactorial(6))


def calcSum(n):
    if n <= 1:
        return n
    else:
        return n + calcSum(n - 1)


print('Sum of n numbers down to 17: ', calcSum(5))


##############################################################################
# This function receives a number (n) and returns all numbers less than it classified as odd or even

def oddsAndEnds(n):
    if (n > 0):
        numList = [*range(1, n + 1)]
        numList.reverse()
        for num in numList:
            if num % 2 == 0:
                print("Even number: " + str(num))
            else:
                print("Odd number: " + str(num))


oddsAndEnds(10)


def oddsAndEndsWhile(n):
    while (n > 0):
        if n % 2 == 0:
            print("Even number: " + str(n))
        else:
            print("Odd number: " + str(n))
        n = n - 1


oddsAndEndsWhile(10)
