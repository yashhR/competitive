t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    first, second = 0, n - 1
    maxi = 0
    while first < second:
        if arr[first] <= arr[second]:
            maxi = max(maxi, second - first)
            first += 1
            second = n - 1
        else:
            second -= 1
    print(maxi)
    t -= 1

'''
Input:
1
9
34 8 10 3 2 80 30 33 1

Output:
6
'''