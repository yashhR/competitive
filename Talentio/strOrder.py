c = []
ans = []
L = list(map(str, input().split()))

for i in L:
    su = 0
    for j in range(len(i)):
        su = su + int(i[j])
        c.append(su)
s = 0

for i in range(len(c)):
    x=[]
    x.append(c[s])
    x.append(L[s])
    ans.append(x)
    s+=1

ans = sorted(ans)
for i in range(len(ans)):
    print(ans[i][1], end = " ")