'''
You are in an infinite 2D grid where you can move in any of the 8 directions:
 (x,y) to
    (x+1, y), (x-1, y), (x, y+1), (x, y-1), (x-1, y-1), (x+1,y+1), (x-1,y+1), (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps
in which you can achieve it. You start from the first point.

Input :
Given two integer arrays A and B, where A[i] is x coordinate and B[i] is y coordinate of ith point respectively.

Output :
Return an Integer, i.e minimum number of steps.
Example :

Input : [(0, 0), (1, 1), (1, 2)]
Output : 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
'''
from itertools import product
allMovements = {}
A = [3, 0, 0, 1]
B = [3, 0, 2, 1]


def all_sides(x, y):
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x-1, y-1), (x+1, y+1), (x-1, y+1), (x+1, y-1)]


def can_move(a, b, cur):
    if (a[i+1], b[i+1]) in all_sides(curr[0], curr[1]):
        return True
    else:
        return False


i = 0
curr = (A[i], B[i])
steps = 0

while i < len(A)-1:
    if can_move(A, B, curr):
        curr = (A[i+1], B[i+1])
        i += 1
        steps += 1
    else:
        if curr[0] > A[i+1]:
            if curr[1] > B[i+1]:
                curr = (curr[0]-1, curr[1]-1)
            elif curr[1] == B[i+1]:
                curr = (curr[0]-1, curr[1])
            else:
                curr = (curr[0]-1, curr[1]+1)
        elif curr[0] == A[i+1]:
            if curr[1] > B[i+1]:
                curr = (curr[0], curr[1]-1)
            elif curr[1] == B[i+1]:
                curr = (curr[0], curr[1])
            else:
                curr = (curr[0], curr[1]+1)
        else:
            if curr[1] > B[i+1]:
                curr = (curr[0]+1, curr[1]-1)
            elif curr[1] == B[i+1]:
                curr = (curr[0]+1, curr[1])
            else:
                curr = (curr[0]+1, curr[1]+1)
        steps += 1
print(steps)

