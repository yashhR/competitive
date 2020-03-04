testCase = int(input())
def minimalArray():
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    mini = min(array)
    lol = array.index(mini)
    shit = sorted(array)
    secondMini = shit[1]
    lol1 = array.index(secondMini)
    if lol == k:
        for i in range(k):
            array[lol], array[lol - 1] = array[lol - 1], array[lol]
            lol = lol - 1
    elif lol1 == k:
        for i in range(k):
            array[lol1], array[lol1 - 1] = array[lol1 - 1], array[lol1]
            lol1 = lol1 - 1
    for i in array:
        if i == array[len(array) - 1]:
            print(i)
        else:
            print(i, end=" ")

for i in range(testCase):
    minimalArray()


