def solve(text1, text2):
    dp = [[0 for x in range(len(text1) + 2)] for x in range(len(text2) + 2)]
    for i1 in range(2, len(text2)+2):
        for i2 in range(2, len(text1)+2):
            # print(text1[i2 - 2], text2[i1 - 2])
            if text1[i2 - 2] == text2[i1 - 2]:
                dp[i1][i2] = 1 + dp[i1-1][i2-1]
            else:
                dp[i1][i2] = max(dp[i1-1][i2], dp[i1][i2-1])
        # for each in dp:
        #     print(each)
    return dp[-1][-1]

print(solve("aggtab", "gxtxayb"))