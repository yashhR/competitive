import itertools
s1, s2 = input().split()
# print(s1, s2)

def no_vowels(some):
    for c in some:
        if c in 'aeiouAEIOU':
            return False
    return True

def Sub_Sequences(STR):
    combs = []
    ret = []
    for l in range(1, len(STR)+1):
        combs.append(list(itertools.combinations(STR, l)))
    for each in combs:
        for i in range(len(each)):
            if no_vowels(each[i]):
                each[i] = ''.join(each[i])
                ret.append(each[i])
    return ret

def intersection(lst1, lst2):
    lst3 = [list(filter(lambda x: x in lst1, sublist)) for sublist in lst2]
    return lst3

subsA = Sub_Sequences(s1)
# print(subsA)
subsB = Sub_Sequences(s2)
# print(subsB)
subs = intersection(subsA, subsB)
for i in range(len(subs)):
    subs[i] = ''.join(subs[i])
# print(subs)
subs.sort(key = lambda x: len(x))
# print(subs)

print(len(subs[-1]))