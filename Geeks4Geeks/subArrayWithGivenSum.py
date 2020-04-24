t = int(input())
while t:
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    seen_sums = {0: 0}
    cum_sum = 0
    found = False
    for i in range(len(arr)):
        # print(seen_sums)
        cum_sum += arr[i]
        # print(f"Is {cum_sum-s} seen before?")
        if cum_sum - s in seen_sums:
            found = True
            print(seen_sums[cum_sum - s] + 1, i + 1)
            break
        seen_sums[cum_sum] = i + 1
    if not found:
        print(-1)
    t -= 1

'''
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5
'''