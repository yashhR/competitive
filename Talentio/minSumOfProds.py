arraySize, modifications = map(int(input().split(" ")))
firstArray = list(map(int, input().split()))
secondArray = list(map(int, input().split()))
indexOfMax = 0
maxi = secondArray[0]
for i in secondArray:
    if abs(i) > maxi:
        maxi = abs(i)
        indexOfMax = secondArray.index(i)
if secondArray[indexOfMax] > 0:
    for i in range(modifications):
        firstArray[indexOfMax] -= 2
elif secondArray[indexOfMax] < 0:
    for i in range(modifications):
        firstArray[indexOfMax] += 2
sums = 0
for i in range(arraySize):
    sums += firstArray[i]*secondArray[i]
return sums


