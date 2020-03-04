#assignment
'''def main():
    num = int(input())
    def fiboc(sn):
        if sn<=1:
            return sn
        else:
            return fiboc(sn-1)+fiboc(sn-2)
    print(fiboc(num))

import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
# 0,1,1,2,3,5,8,13,21,34,55,89,144,233'''
'''
1) Primes that can be expressed as sum of consecutive prime numbers within 3 to given range
input   output   explanation
20      2        below 20, there are 2 such numbers: 5 and 17
                 5 = 2+3
                 17 = 2+3+5+7

15      1       5 = 2+3


2)
find min sum of prods of 2 arrays of same size, given k modifications are allowed on 1st array.
in each modification, one array element of 1st array can be either decremented or incremented by 2





input       output  explanation
3 5         -31     no.of elements =3; no. of modifications = 5
1 2 -3              -3 is A[2], incremented by 2(5 times) = 7
-2 3 -5             (1*-2) + (2*3) + (7*-5) = -31


5 3                 3 is A[1], decremented by 2(3 times) = -3
2 3 4 5 4   25      (2*3) + (-3*4) + (4*2) + (5*3) + (4*2) = 25
3 4 2 3 2



C compilers for the pre-increment post-increment question

In printf(), the executor checks from right to left, does the operator in its way and it prints from left to right

 

'''
'''
Denmaaarkk
D1e1n1m1a3r1k2

raccceeeccd
r1a1c3e3c2d1

from collections import Counter
word = list(input())
col = Counter(word)
for i in col:
    if col[i]>0:
        print(f"{i}{col[i]}",end="")
'''
'''
word = input()
k = len(word)
lol = []
for i in range(k):
    c = 0
    if word[i] == word[k-1]:
        c = 1
    elif word[i] == '/':
        
    else:
        c = 1
        if word[i] == word[i+1]:
            while word[i+1] != word[i]:
                c += 1
                i += 1
            word.replace(word[i],'/',c)
    lol.append(c)
for i in range(len(word)):
    print(word[i], end="")
    print(lol[i], end="")
'''

word = input()
l = []
l1 = []
l1.append(word[0])
l2 = []
c = 1
for i in range(len(word)):
    if word[i] == l1[-1]:
        c += 1
    elif word[i] != l1[-1]:
        l1.append(word[i])
        l2.append(c)
        c = 0
        c += 1

for i in range(len(l1)):
    print(l1[i], end='')
    print(l2[i], end='')
