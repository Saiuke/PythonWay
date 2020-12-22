def myRange(a, b):
    while a < b:
        yield a
        a += 1

lousaSuja = myRange(2,18)
print(next(lousaSuja))
print(next(lousaSuja))
print(list(myRange(3,19)))

def yieldOdds(n):
    for i in range(n):
        if i % 2 == 1:
            yield i

for n in yieldOdds(33)
    print(n)
