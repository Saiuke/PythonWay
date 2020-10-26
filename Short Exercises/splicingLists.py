list = [10, 23, 47, 89, 52, 63, 98, 74, 41, 54]
print(list[7:])
list[2:5] = [88, 55, 44]
print(list)
# Nested lists
nestList = \
    [
        [20, 58, 45, 39],
        [74, 32, 12, 77],
        [11, 19, 17, 13],
    ]
print(nestList)
for item in nestList:
    print(item)
print(nestList[-1:])


##########################################################################

def sortParity(list):
    pairList = []
    oddList = []
    for item in list:
        if item % 2 == 0:
            pairList.append(item)
        else:
            oddList.append(item)
    return [pairList, oddList]


##########################################################################

def getAverage(list):
    sumaEl = 0
    for el in list:
        sumaEl += el
    return (sumaEl / len(list))


##########################################################################

# Remove certain elements of a list
def listChanger(list, remove):
    for el in remove:
        if el in list:
            list.remove(el)
    return list


print(sortParity(list))
print(getAverage(list))
print(listChanger(list, [89, 52, 41, 10]))
print([x * x for x in list])  # Calculate the square of each number in a list


##########################################################################

def transposeMatrix(matrix):
    matrixSize = len(matrix[0])
    transposedMatrix = []
    for i in range(matrixSize):
        transposedRow = []
        for row in matrix:
            transposedRow.append(row[i])
        transposedMatrix.append(transposedRow)
    return transposedMatrix


[print(row) for row in transposeMatrix(nestList)]

##########################################################################

# The same could be done using [[row[i] for row in matrix] for i in range(4)]

# Fuck this shit, apparently this following line does the same thing too
[print(row) for row in zip(*nestList)]


def calculateCube(list):
    return [x ** 3 for x in list]


print(calculateCube(list))

##########################################################################

# Writes all even and odd numbers there are <= given number
def oddsAndEvens(maxNumber):
    odds = [x for x in range(maxNumber) if (x % 2 != 0)]
    even = [x for x in range(maxNumber) if (x % 2 == 0)]
    # The above line can also be done like this: [x for x in range(maxNumber) if (x not in odds)]
    return [even, odds]


print(oddsAndEvens(200))

novaLista = [41, 53, 65, 45, 89, 91, 32, 21, 19, 11, 5, 77, 14]

##########################################################################

# Retorna a soma dos membros de uma lista
def sumList(list):
    sum = 0
    [sum := sum + x for x in list]
    return sum


print("A soma da lista é: ", sumList(novaLista))

# The same can be accomplished using sum(list)
print(sum(novaLista))

##########################################################################

# Given a getSquare() function, make a list comprehension that returns a list with the squares of all even numbers from 0 to 20, but ignores those numbers that are divisible by 3.

def ignoreDivisibles(list):
    output = [x * x for x in list if (x % 3 != 0) and (x % 2 == 0)]
    return output


print(ignoreDivisibles(novaLista))

##########################################################################

# Finds the greater number in a list (I know that's not the most efficient way)

def maxInList(list):
    maxNum = None;
    for el in list:
        if (maxNum == None) or (maxNum < el):
            maxNum = el
            print(maxNum)
    return maxNum

print(maxInList(novaLista))

##########################################################################

listaTeste = [4, 2, 3, 1]

#Sort out list

def sortList(list):
    listSize = len(list)
    for i, el in enumerate(list):
            if i < listSize:
                if el > list[i+1]:
                    list.insert(i, list.pop(i+1))
                    print(list)
    return list

sortList(listaTeste)



