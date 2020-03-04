def setZeroes(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 0:
                for k in range(len(a[i])):
                    a[i][k] = 0
                for k in range(len(a)):
                    a[k][j] = 0
                return a

a = [[1, 0, 1],[1, 1, 1], [1, 1, 1]]

print(setZeroes(a))