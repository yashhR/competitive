'''
n = 7
matrix = [['.', '.', '.', '.', '.', '.', '.'],
          ['.', '*', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.']]

star = [0, 0]
for i in range(n):
    for j in range(n):
        if matrix[i][j] == "*":
            star = [i, j]
            break

ans = (n//2 - star[0]) + (n//2 - star[1])

print(ans)
'''

n = int(input())
matrix = []
x = []
star = [0, 0]
for i in range(n):
    x.append(input())
    matrix.append(x)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == "*":
            star = [i, j]
            break

print(star)