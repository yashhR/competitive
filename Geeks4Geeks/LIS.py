t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()))
    dp = [1 for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))
    t -= 1

'''  
0 1 2 3 4 5 6 7 
1 2 3 7 5 9 4 8


'''