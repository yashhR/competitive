t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    pos = True
    length = 1
    if array[0] > 0:
        pos = True
        least = array[0]
    else:
        pos = False
        maxi = array[0]
    result = 0
    for i in range(1, len(array)):
        if pos:
            if array[i] < 0:
                maxi = array[i]
                result += least
                length += 1
                pos = not pos
                if i == n - 1:
                    result += maxi
            else:
                least = max(least, array[i])
                if i == n - 1:
                    result += least
        else:
            if array[i] > 0:
                least = array[i]
                result += maxi
                length += 1
                pos = not pos
                if i == n - 1:
                    result += least
            else:
                maxi = max(maxi, array[i])
                if i == n - 1:
                    result += maxi
    if length == n:
        print(sum(array))
    elif length == 1:
        print(max(array))
    else:
        print(result)
