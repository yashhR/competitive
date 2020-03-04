from itertools import combinations

A = [1, 1, 1, 2, 2]

combs = list(combinations(A, r = 3))

lols = list(map(list, combs))
print(lols)
number = 0
for i in lols:
    count = 0
    for j in i:
        if j < sum(i)-j:
            count += 1
        else:
            break
    if count == 3:
        number += 1
print(number)
