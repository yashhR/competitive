'''
Given an integer n, print all beautiful numbers within the range n
A beautiful number is a number which either has a single digit or a single digit repeating itself
Ex: All single digit numbers are beautiful numbers, 11,22,33,666,9999,1111111
'''

def isBeautifuL(num):
    flag = None
    lol = str(num)
    if len(lol) == 1:
        return 1
    else:
        for i in range(len(lol)-1):
            if lol[i] == lol[i+1]:
                flag = 1
                continue
            else:
                flag = 0
                break
        if flag:
            return 1
        else:
            return 0
bro = int(input())
count = 0
for i in range(1, bro+1):
    if isBeautifuL(i):
        #print(i)
        count += 1
print(count)