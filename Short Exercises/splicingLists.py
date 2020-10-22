list = [10, 23, 45, 89, 52, 63, 98, 74, 41, 54]
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


def sortParity(list):
    pairList = []
    oddList = []
    for item in list:
        if item % 2 == 0:
            pairList.append(item)
        else:
            oddList.append(item)
    return [pairList, oddList]


def getAverage(list):
    sumaEl = 0
    for el in list:
        sumaEl += el
    return (sumaEl / len(list))


# Remove certain elements of a list
def listChanger(list, remove):
    for el in remove:
        if el in list:
            list.remove(el)
    return list


print(sortParity(list))
print(getAverage(list))
print(listChanger(list, [89, 52, 41, 10]))
print([x * x for x in list])  # Calculate the square of each number in list


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

# The same could be done using [[row[i] for row in matrix] for i in range(4)]

# Fuck this shit, apparently this following line does the same thing too
[print(row) for row in zip(*nestList)]
