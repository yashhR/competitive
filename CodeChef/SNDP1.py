t = int(input())
while t:
    n, b, m = map(int, input().split())
    access = list(map(int, input().split()))
    ans = 0
    first = True
    for each in access:
        if first:
            first = False
            ans += 1
            prev = each
        else:
            if prev // b != each // b:
                ans += 1
                prev = each
    print(ans)
    t -= 1

"""
4

20

0, 1, 2, 3 = 0, 0, 0, 0
4, 5, 6, 7 = 1, 1, 1, 1
8, 9, 10, 11 = 2, 2, 2, 2
12, 13, 14, 15 = 3, 3, 3, 3
16, 17, 18, 19 = 4, 4, 4, 4
"""