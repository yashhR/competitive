
from itertools import permutations
a, b = input().split(" ")
l = []
for i in a:
    l.append(i)
x = permutations(l)
new = []
for i in x:
    if len(new)==0:
        if int(''.join(i)) > int(b):
            new.append(int(''.join(i)))
    else:
        if int(''.join(i)) > int(b) and int(''.join(i)) < new[-1]:
            new.append(int(''.join(i)))
print(new)
if len(new) == 0:
    print(-1)
else:
    print(min(new))
