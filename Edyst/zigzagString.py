import itertools
def convert(A, B):
    l = []
    matrix = []
    for i in range(B):
        matrix.append([])
        l.append(i)
    for i in range(B-2, 0, -1):
        l.append(i)
    iterators = itertools.cycle(l)
    for i in A:
        matrix[next(iterators)].append(i)
    res = ''
    for i in matrix:
        res += ''.join(i).rstrip()
    return res
print(convert("zigzagstring", 3))