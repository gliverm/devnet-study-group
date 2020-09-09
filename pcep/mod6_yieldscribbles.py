def powersOf2(n):
    pow = 1
    for i in range(n):
        yield pow
        pow *= 2


for v in powersOf2(8):
    print(v)

t = [x for x in powersOf2(5)]

print(t)

t = list(powersOf2(3))

print(t)

for i in range(20):
    if i in powersOf2(4):
        print(i)

def Fib(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(Fib(10))

print(fibs)