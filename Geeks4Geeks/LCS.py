t = int(input())
while t:
    a, b = map(int, input().split())
    ans = 0
    s1 = input()
    s2 = input()

    def lcs(s1, s2):
        global ans
        if len(s1) and len(s2):
            if s1[-1] == s2[-1]:
                return 1 + lcs(s1[:-1], s2[:-1])
            else:
                return max(lcs(s1, s2[:-1]), lcs(s1[:-1], s2))
        else:
            return 0

    lcs(s1, s2)

    print(ans)
    t -= 1