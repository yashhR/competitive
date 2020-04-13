from itertools import combinations

s1, s2 = input().split()


set1 = set(s1)
set2 = set(s2)


set1 = set1.intersection(set2)

set1 = list(set1)
print(set1)
set1[:] = [x for x in set1 if x not in set("AEIOUaeiou")]
print(set1)
# possis = []
#
# for i in range(1, len(set1)):
#     possis.append(list(combinations(set1, r=i)))
#
# for i in range(len(possis)):
#     possis[i] = ''.join(possis[i])

