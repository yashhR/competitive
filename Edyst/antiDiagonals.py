def Solution(A):
    result = []
    diagonal = []
    n = len(A)
    if n == 0:
        return result
    for d in range((2*(n-1))+1):
        for i in range(d+1):
            j = d - i
            if i >= n or j >= n:
                continue
            diagonal.append(A[i][j])
        result.append(diagonal)
        diagonal = []
    return result

print(Solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))