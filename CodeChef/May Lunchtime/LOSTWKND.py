t = int(input())
while t:
    info = list(map(int, input().split()))
    p = info[-1]
    info.pop(-1)
    work = list(map(lambda x: x*p, info))
    for i in range(5):
        if i == 4:
            if work[i] > 24:
                print("Yes")
            else:
                print("No")
            break
        elif work[i] > 24:
            work[i+1] += work[i] - 24
        elif work[i] < 24:
            work[i+1] -= 24 - work[i]
    t -= 1