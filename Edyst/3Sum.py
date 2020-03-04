from itertools import combinations
def three_sum(a, b):
    prods = combinations(a, r=3)
    sums = []
    for each in prods:
        sums.append(sum(each))
    mini = 100000
    diffs = []
    for i in sums:
        diffs.append(abs(b-i))
    return b - min(diffs)


print(three_sum([-15, -7, 5, 4, -11, -9, -2], -11))