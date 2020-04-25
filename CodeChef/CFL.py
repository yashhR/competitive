t = int(input())
while t:
    n, s = map(int, input().split())
    players = list(map(int, input().split()))
    roles = list(map(int, input().split()))
    forwardLeast = 9999999999999
    leastdef = 9999999999999
    f = 0
    d = 0
    for i in range(n):
        if roles[i] == 1:
            f = 1
            forwardLeast = min(forwardLeast, players[i])
        else:
            leastdef = min(leastdef, players[i])
            d = 1
    if f and d:
        if s + forwardLeast + leastdef <= 100:
            print("yes")
        else:
            print("no")
    else:
        print("no")
    t -= 1