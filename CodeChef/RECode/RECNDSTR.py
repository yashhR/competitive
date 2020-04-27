t = int(input())
while t:
    s = input()
    s = list(s)
    a = s[:]
    b = s[:]
    a.append(a.pop(0))
    b.insert(0, b.pop())
    if a == b:
        print("YES")
    else:
        print("NO")
    t -= 1