t = int(input())
while t:
    n, q = map(int, input().split())
    s = input()
    freq = {}
    uniques = 0
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
            uniques += 1
    while q:
        c = int(input())
        if c == 0:
            print(n)
        elif c == 1:
            print(n-uniques)
        else:
            okay = sorted(freq.items(), key=lambda x: x[1])
            if okay[-1][1] <= c:
                print(0)
            else:
                p = 0
                for each in okay[::-1]:
                    if each[1] > c:
                        p += each[1] - c
                    else:
                        break
                print(p)
        q -= 1
    t -= 1