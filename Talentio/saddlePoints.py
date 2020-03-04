rows,cols = 5,5
array = []
for i in range(rows):
    a = list(map(int, input()))
    array.append(a)


def findSaddle(array):
    maxArray = []
    for i in array[0]:
        i.append(maxArray)
    x = max(maxArray)
    for i in array[][0]:
        i.append(minArray)
    y = min(minArray)
    if x == y:
        print(f"{x},{y}")

