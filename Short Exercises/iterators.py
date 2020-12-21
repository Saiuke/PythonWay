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
