from itertools import product
def binnBig(x):
    res = ''
    while x != 0:
        bro = x % 2
        res = res + str(bro)
        x = x // 2
    return res[::-1].zfill(8)
def binnSmall(x):
    res = ''
    while x!=0:
        bro = x%2
        res = res + str(bro)
        x = x//2
    return res[::-1].zfill(4)
def d(X, Y):
    if X == Y:
        return(0)
    elif X>15 or Y>15:
        count = 0
        binx = binnBig(X)
        biny = binnBig(Y)
        for i, j in zip(binx, biny):
            if i != j:
                count += 1
        return(count)
    else:
        count = 0
        binx = binnSmall(X)
        biny = binnSmall(Y)
        for i, j in zip(binx, biny):
            if i != j:
                count += 1
        return (count)

A = [99, 85, 43, 74, 38, 70, 36, 22, 13, 82]
combs = product(A, repeat=2)
sumi = 0
for i in combs:
    (x, y) = i
    sumi += d(x, y)
print(sumi)