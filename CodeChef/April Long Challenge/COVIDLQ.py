t = int(input())
for _ in range(t):
    n = int(input())
    q = list(map(int, input().split()))
    found = False
    bitch = False
    for i in range(len(q)):
        if q[i] == 1:
            if not found:
                found = True
                prev = i
            else:
                if i - prev < 6:
                    bitch = True
                    print("NO")
                    break
                else:
                    prev = i
    if not bitch:
        print("YES")

