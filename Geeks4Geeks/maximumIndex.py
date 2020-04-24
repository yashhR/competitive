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
Main opti point:
First pointer goes through every element from the beginning, and for every element, the second pointer starts from the
end because we want to find the farthest index where the first element is lesser than second.

So, mop is starting from the end.
'''
'''
Input:
1
9
34 8 10 3 2 80 30 33 1

Output:
6
'''