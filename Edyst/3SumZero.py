from itertools import combinations
def threeSum(A):
    combs = combinations(A, r=3)
    poss = []
    for i in combs:
        if sum(i) == 0:
            poss.append(list(i))
    for i in poss:
        i.sort()
    temp = []
    [temp.append(x) for x in poss if x not in temp]
    temp.sort()
    return temp

print(threeSum([-1, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 1]))