'''
For each N, print the trailing zeroes at the end of it's factorial
'''

from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    factor = 5
    ans = 0
    while factor <= n:
        ans += n//factor
        factor *= 5
    print(ans)


