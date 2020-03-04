def lol():
    noOfSides, noOfFriends = map(int, input().split())
    for i in range(noOfFriends):
        if noOfSides==3:
            break
        elif noOfSides%2==0:
            noOfSides = noOfSides//2 + 1
        else:
            noOfSides = noOfSides//2 + 2
    print(noOfSides)
testCases = int(input())
for i in range(testCases):
    lol()