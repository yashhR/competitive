t = int(input())
while t:
    a, b, q = map(int, input().split())
    while q:
        l, r = map(int, input().split())
        c = 0
        for i in range(l, r+1):
            if i % a == 0 or i % b == 0:
                c += 1
        print(abs(l-r) - c)
        q -= 1
    t -= 1
