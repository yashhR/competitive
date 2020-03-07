class Solution:
    def longestCommonPrefix(self, A):
        n = min([len(x) for x in A])
        if len(A) == 1:
            return A[0]
        else:
            def is_same(x):
                flag = 0
                for i in range(len(A)-1):
                    if A[i][:x] == A[i+1][:x]:
                        flag = 1
                    else:
                        flag = 0
                        break
                if flag:
                    return True
                else:
                    return False
            for j in range(n, 0, -1):
                if is_same(j):
                    return A[0][:j]
            return ''