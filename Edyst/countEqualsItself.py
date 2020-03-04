def solve(A):
    res = -1
    for i in range(len(A)):
        count = 0
        for j in range(len(A)):
            print(A[i], A[j],end=" ")
            if A[i] > A[j]:
                count += 1
                print(count)
        if count == A[i]:
            res = 1
            break
    return res

print(solve([4, -9, 8, 5, -1, 7, 5, 3]))