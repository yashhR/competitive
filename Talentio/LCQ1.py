def thirt(n):
    rems = [1, 10, 9, 12, 3, 4]
    bro = 0
    k = len(str(n))
    for i in range(k):
        if i < len(rems):
            bro += rems[i] * int(str(n)[k - i - 1])
        else:
            bro += rems[len(rems)-i] * int(str(n)[k - i - 1])
    p = bro
    if bitch[-1] == p:
        return p
    bitch.append(p)
    return thirt(p)
bitch = [0]
print(thirt(321))