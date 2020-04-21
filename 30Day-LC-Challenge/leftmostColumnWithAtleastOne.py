'''
(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.



Example 1:



Input: mat = [[0,0],[1,1]]
Output: 0
Example 2:



Input: mat = [[0,0],[0,1]]
Output: 1
Example 3:



Input: mat = [[0,0],[0,0]]
Output: -1
Example 4:



Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1


Constraints:

1 <= mat.length, mat[i].length <= 100
mat[i][j] is either 0 or 1.
mat[i] is sorted in a non-decreasing way.
'''

def solution(binaryMatrix):
    dimensions = BinaryMatrix.dimensions()
    n = dimensions[0]
    m = dimensions[1] - 1
    found = False
    for row in range(n):
        if not found:
            if BinaryMatrix.get(row, m) == 1:
                found = True
                least = m
                while least > -1 and BinaryMatrix.get(row, least) == 1:
                    least -= 1
                if least == 0:
                    if BinaryMatrix.get(row, least) == 1:
                        return 0
                    else:
                        least += 1
                else:
                    least += 1
        else:
            if BinaryMatrix.get(row, least) == 1:
                while least > -1 and BinaryMatrix.get(row, least) == 1:
                    least -= 1
                if least == 0:
                    if BinaryMatrix.get(row, least) == 1:
                        return 0
                    else:
                        least += 1
                else:
                    least += 1
    if not found:
        return -1
    else:
        return least


print(solution([[0,0,0,1],[0,0,1,1],[0,1,1,1]]))
