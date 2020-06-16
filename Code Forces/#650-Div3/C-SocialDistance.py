t = int(input())
while t:
    n, k = map(int, input().split())
    s = list(input())
    ans = 0
    i = 0
    while i < n:
        if s[i] == "0":
            idx = i + 1
            temp = k
            givePass = True
            while temp and idx < n:
                if s[idx] == "1":
                    givePass = False
                    break
                else:
                    idx += 1
                    temp -= 1
            if givePass:
                s[i] = "1"
                ans += 1
                i += k + 1
            else:
                i += 1
        else:
            i += k + 1
    print(ans)
    t -= 1