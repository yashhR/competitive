class Solution:
    def searchRange(self, a, b):
        # write your method here
        key=b
        c=[]
        for i in range(len(a)):
            if(a[i]==key):
                c.append(i)
        if(len(c)==0):
            c.append(-1)
            c.append(-1)
        elif(len(c)==1):
            d=c.pop()
            c.append(d)
            c.append(d)
        return c