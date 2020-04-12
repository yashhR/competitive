t = int(input())
while t:
    n = int(input())
    sids = []
    ress = []
    while n:
        sid, res = map(int, input().split())
        sids.append(sid)
        ress.append(res)
        n -= 1
    count = 0
    i = 0
    prev = -1
    conOnes = []
    while i < len(ress):
        if ress[i] == 1:
            start = i
            count = 0
            while i < len(ress) and ress[i] == 1:
                count += 1
                i += 1
            if i == len(ress) - 1:
                conOnes.append((count, (start, i+1)))
            else:
                conOnes.append((count, (start, i)))
        else:
            i += 1
    ans = 0
    print(f"IDs: {sids}")
    print(f"Results: {ress}")
    print(f"Continuous ones count and indices: {conOnes}")
    for each in conOnes:
        print(f"IDs part of the {each} indices are {sids[each[1][0]:each[1][1]]} and unique ids are {set(sids[each[1][0]:each[1][1]])},"
              f"and hence the length is {len(set(sids[each[1][0]:each[1][1]]))}")
        ans = max(ans, len(set(sids[each[1][0]:each[1][1]])))
    print(ans)
    t -= 1