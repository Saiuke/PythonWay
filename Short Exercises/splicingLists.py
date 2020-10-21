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


print(sortParity(list))
