def myRange(a, b):
    while a < b:
        yield a
        a += 1


lousaSuja = myRange(2,18)
print(next(lousaSuja))
print(next(lousaSuja))
print(list(myRange(3,19)))

def yieldOdds(k):
    for i in range(k):
        if i % 2 == 1:
            yield i


print(list(yieldOdds(19)))


def downToZero(n):
    for i in range(n, -1, -1):
        yield i


for i in downToZero(14):
    print(i)

