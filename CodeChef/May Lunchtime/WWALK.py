t = int(input())
while t:
    n = int(input())
    aspeed = list(map(int, input().split()))
    bspeed = list(map(int, input().split()))
    apos = 0
    bpos = 0
    wd = 0
    for i in range(0, n):
        if aspeed[i] == bspeed[i] and apos == bpos:
            wd += aspeed[i]
        apos += aspeed[i]
        bpos += bspeed[i]
    print(wd)
    t -= 1