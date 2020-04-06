t = int(input())
for _ in range(t):
    n = int(input())
    types = []
    while n:
        type = list(map(int, input().split()))
        types.append(type)
        n -= 1
    maximum_profit = 0
    for type in types:
        if type[1] >= type[0] + 1:
            maximum_profit = max(maximum_profit, (type[1]//(type[0]+1)) * type[2])
    print(maximum_profit)