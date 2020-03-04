#def countAndSay(n):
from collections import Counter
lol = [1, 11, 21, 1121]
for i in range(n):
    s = ''
    for i in str(lol[-1]):
        cnt = str(lol[-1]).count(i)
        s += f"{cnt}{i}"
    lol.append(int(s))
    print(lol)
