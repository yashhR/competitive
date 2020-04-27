t = int(input())
while t:
    n = int(input())
    types = list(map(int, input().split()))
    prevIndices = {}
    count = {}
    for i in range(n):
        if types[i] not in prevIndices:
            prevIndices[types[i]] = i
            count[types[i]] = 1
        else:
            if i != prevIndices[types[i]] + 1:
                prevIndices[types[i]] = i
                count[types[i]] += 1
    maxi = -1
    # print(count)
    for type in count.keys():
        if count[type] > maxi:
            maxi = count[type]
            ans = type
        elif count[type] == maxi:
            if type < ans:
                ans = type
    print(ans)
    t -= 1