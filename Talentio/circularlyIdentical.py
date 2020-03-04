# check if the firstList is circularly Identical to the second one

firstList = input().split()
secondList = input().split()

for i in range(len(firstList)):
    flag = 0
    k = secondList.pop()
    secondList.insert(0, k)
    if secondList == firstList:
        flag = 1
        break

if flag:
    print("Yes")
else:
    print("No")

