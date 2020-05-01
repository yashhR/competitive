t = int(input())
while t:
    n, m = map(int, input().split())
    perm = list(map(int, input().split()))
    pairs = set()
    while m:
        x, y = map(int, input().split())
        pairs.add((x, y))
        m -= 1
    actual = [x for x in range(1, n+1)]
    minutes = -1
    for i in range(len(actual)):
        # print(f"current position of {actual[i]}: {i+1}, desired position: {perm[i]}")
        if i + 1 == perm[actual[i] - 1]:
            continue
        else:
            k = actual[i]
            if (i+1, perm[k-1]) in pairs:
                actual[i], actual[perm[k - 1] - 1] = actual[perm[k - 1] - 1], actual[i]
            else:
                actual[i], actual[perm[k - 1] - 1] = actual[perm[k - 1] - 1], actual[i]
                minutes += 1
    print(minutes)
    t -= 1