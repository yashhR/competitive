s = '2(3(NW)2(W2(EE)W))'
ans = ''
hehe = []
found = False
for c in s:
    if c in set('123456789'):
        found = True
    if c == ')':
        temp = ''
        while hehe[-1] != '(':
            temp += hehe.pop()
        temp = temp[::-1]
        hehe.pop()
        temp = int(hehe.pop())*temp
        ans += temp
        found = False
    else:
        if not found:
            ans += c
        hehe.append(c)
print(ans)
