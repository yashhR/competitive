'''
You are given four positive integers a, b, c, d, such that a≤b≤c≤d.

Your task is to find three integers x, y, z, satisfying the following conditions:

a≤x≤b.
b≤y≤c.
c≤z≤d.
There exists a triangle with a positive non-zero area and the lengths of its three sides are x, y, and z.

1 3 5 7

1 3
'''

t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    