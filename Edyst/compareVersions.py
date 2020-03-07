class Solution:
    def compareVersion(self, A, B):
        a=list(map(int,A.split('.')))
        x=len(a)
        b=list(map(int,B.split('.')))
        y=len(b)
        while(x>y):
            b.append(0)
            y+=1
        while(y>x):
            a.append(0)
            x+=1
        if a>b:
            return 1
        if a<b:
            return -1
        return 0