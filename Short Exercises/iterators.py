newIter = iter([1, 2, 3, 4])
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
        for i in range(1, self.n + 1):
            if i % 2 == 0:
                evenNumbers.append(i)
            else:
                i += 1
        return evenNumbers


newEven = EvenRange(19)
print(newEven.next())


class DownZero():
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        downZeroList = []
        if self.n == 0:
            downZeroList.append(self.n)
            return downZeroList
        else:
            while self.n > 0:
                downZeroList.append(self.n)
                self.n -= 1
            downZeroList.append(self.n)
            return downZeroList


goDown = DownZero(2)
print(goDown.next())


class CalcFibo:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        fiboSequence = []
        for i in range(self.n):
            if i == 0 or i == 1:
                fiboSequence.append(i)
            else:
                fiboSequence.append(fiboSequence[i - 2] + fiboSequence[i - 1])
        return fiboSequence

newFibo = CalcFibo(18)
print(newFibo.next())
