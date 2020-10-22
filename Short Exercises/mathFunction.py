# Returns the GDC of 2 two integers
def findGCD(a, b):
    minNumber = a if a < b else b
    minNumber = minNumber if minNumber > 0 else minNumber * -1 #Ensures that minNumber is always positive, like you
    commonDivisors = [ x for x in range(2, minNumber + 1) if (a % x == 0) and (b % x == 0)]
    return max(commonDivisors) if len(commonDivisors) >= 1 else 1

print(findGCD(18, 81))
print(findGCD(12, 4))
print(findGCD(1024, 512))
print(findGCD(15, 2))
print(findGCD(-18, 9))