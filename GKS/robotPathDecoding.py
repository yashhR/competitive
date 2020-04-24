t = int(input())
while t:
    n = 10**9
    s = input()
    ans = ''
    hehe = []
    for c in s:
        if c == ')':
            while hehe[-1] != '(':
                ans += hehe.pop()
            ans = ans[::-1]
            hehe.pop()
            ans = int(hehe.pop())*ans
        else:
            hehe.append(c)
    print(ans)
    s = ans
    n = len(ans)
    w, h = 1, 1
    for i in range(len(s)):
        if s[i] == 'N':
            if h == 1:
                h = n
            else:
                h -= 1
        elif s[i] == 'S':
            if h == n:
                h = 1
            else:
                h += 1
        elif s[i] == 'W':
            if w == 1:
                w = n
            else:
                w -= 1
        elif s[i] == 'E':
            if w == n:
                w = 1
            else:
                w += 1
    print(w, h)
    t -= 1