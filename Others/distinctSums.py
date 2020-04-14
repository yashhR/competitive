import sys
import math
from itertools import combinations
# Print the number of distinct sums.

n = int(input())  # Number of integers in the array.
bitch = list(map(int, input().split()))
bro = []
for i in range(1, n+1):
    bro.append(list(combinations(bitch, r = i)))
new = set()
for i in range(len(bro)):
    for each in bro[i]:
        new.add(sum(each))
print(len(new))
