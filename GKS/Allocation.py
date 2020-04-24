t = int(input())
k = 1
while t:
    n, b = map(int, input().split())
    costs = list(map(int, input().split()))
    costs.sort()
    spent = 0
    i = 0
    ans = 0
    while True and i < len(costs):
        if spent + costs[i] <= b:
            ans += 1
            spent += costs[i]
            i += 1
        else:
            break
    print("Case #" + str(k) + ": " + str(ans))
    k += 1
    t -= 1