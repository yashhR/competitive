from collections import Counter
t = int(input())
while t:
    s = input()
    k = Counter(s)
    if len(k) == 1:
        print(s)
    else:
        s = list(s)
        hehe = s[:]
        inserted = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                hehe.insert(i + inserted, str(1 - int(s[i])))
                inserted += 1
        print(''.join(hehe))
    t -= 1
