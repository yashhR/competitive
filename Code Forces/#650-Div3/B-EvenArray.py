"""
If it's an odd length array, even indices will be one more than the odd indices, but if its an even length array,
odd indices and even indices will be the same number.
"""

t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    evenMis, oddMis = 0, 0
    for i in range(n):
        if arr[i] % 2 != i % 2:
            if i % 2 == 0:
                evenMis += 1
            else:
                oddMis += 1
    if evenMis == oddMis:
        print(evenMis)
    else:
        print(-1)
    t -= 1