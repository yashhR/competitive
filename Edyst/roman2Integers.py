def romanToInt(A):
    res = 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(A)):
        if i == len(A)-1:
            res += dict[A[i]]
        else:
            if dict[A[i]] >= dict[A[i + 1]]:
                res += dict[A[i]]
            else:
                res -= dict[A[i]]
    return res

print(romanToInt("IV"))