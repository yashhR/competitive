t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = []
    count = 0
    i = 0
    while i < len(arr):
        if i == len(arr) - 1:
            ans.append(arr[i])
            break
        if count < 2:
            if arr[i] != arr[i+1]:
                count += 1
                ans.append(arr[i])
                i += 1
            else:
                i += 2
        else:
            break
    print(ans[0], ans[1])
    t -=1

'''
Input :
2
2
1 2 3 2 1 4
1
2 1 3 2

Output :
3 4
1 3
'''