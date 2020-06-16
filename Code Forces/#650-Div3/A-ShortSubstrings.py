t = int(input())
while t:
    b = input()
    ans = b[0] + b[1]
    l = len(b)
    if l > 2:
        for i in range(3, l, 2):
            ans += b[i]
    print(ans)
    t -= 1