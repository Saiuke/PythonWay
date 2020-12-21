newIter = iter([1,2,3,4])
print(next(newIter))
print(next(newIter))
print(next(newIter))



class MyRange:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):
        return self

    def next(self):
        if self.a < self.b:
            value = self.a
            self.a += 1
            return value
        else:
            raise StopIteration

myRange = MyRange(1, 4)
print(myRange.next())
print(myRange.next())
print(myRange.next())

class EvenRange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        evenNumbers = []
        for i in range(1, self.n+1):
            if i % 2 == 0:
                evenNumbers.append(i)
            else:
                i += 1
        return evenNumbers

newEven = EvenRange(19)
print(newEven.next())

