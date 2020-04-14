import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
count = 0
while n % 2 == 0:
    count += 2
    n = n // 2

for i in range(3, n + 1, 2):
    while n % i == 0:
        count += i
        n = n // i

if n > 2:
    count += 2
print(count)