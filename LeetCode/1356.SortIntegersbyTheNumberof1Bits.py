def sortByBits(arr):
    c = []
    for i in arr:
        c.append(bin(i).count('1'))

    for i in range(len(c)):
        for j in range(0, len(c) - i - 1):
            if c[j] > c[j + 1]:
                (c[j], c[j + 1]) = (c[j + 1], c[j])
                (arr[j], arr[j + 1]) = (arr[j + 1], arr[j])
            elif c[j] == c[j + 1]:
                if arr[j] > arr[j + 1]:
                    (arr[j + 1], arr[j]) = (arr[j], arr[j + 1])
    return (arr)