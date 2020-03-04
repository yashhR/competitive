def sum_pairs(ints, s):
    listi = []
    flag = 0
    mini = len(ints) - 1
    for i in ints:
        if s - i in ints[ints.index(i) + 1:]:
            if (ints[ints.index(i)+1:].index(s - i) <= mini):
                mini = ints[ints.index(i)+1:].index(s - i)
                flag = 1
                listi.append((i, s - i))
    print(listi)
    if flag:
        return list(listi[-1])
    else:
        return None
sum_pairs([10, 5, 2, 3, 7, 5],10)