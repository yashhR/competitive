def maximal_square(matrix):
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    maxi, n, m = 0, len(matrix), len(matrix[0])
    dp = [[0 for x in range(m+1)] for x in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if matrix[i-1][j-1] == '1':
                dp[i][j] = min(dp[i-1][j-1], min(dp[i][j-1], dp[i-1][j])) + 1
                maxi = max(maxi, dp[i][j])
    return maxi**2

