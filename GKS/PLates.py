'''
How do I simulate a circle?

[1 2 3 4]
1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4
'''

circle = [1, 2, 3, 4]
n = len(circle)
jump = 4
print(circle[(jump - 1) % n])

