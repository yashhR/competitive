n=int(input())
l=[]
f=[]
f1=[]
for i in range(n):
    l.append(input())
for i in range(n):
    s=''
    for j in range(len(l[i])):
        if(l[i][j]=='/' and l[i][j+1]=='/'):
            s1=''
            for k in range(j, len(l[i])):
                s1=s1+l[i][k]
            f1.append(s1)
            break
        else:
            s=s+l[i][j]
    f.append(s)
for i in range(n):
    f[i] = f[i].replace('-', '.')
    f[i] = f[i].replace('>', '')
for i in range(len(l)):
    print(f[i]+f1[i])