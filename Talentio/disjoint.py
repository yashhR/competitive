def answer():
    checks = list(map(int, input().split()))
    friends = checks[0]
    endingPoint = checks[1]
    maryStart = checks[2]
    maryEnd = checks[3]
    allFriendsIndices = []
    for i in range(friends):
        allFriendsIndices.append(list(map(int, input().split())))
    marysIndices = []
    for i in range(maryStart, maryEnd + 1):
        marysIndices.append(i)
    listsOfAllFriends = []
    for i in range(friends):
        listsOfAllFriends.append([x for x in range(allFriendsIndices[i][0], allFriendsIndices[i][1] + 1)])
    marysSet = set(marysIndices)
    setsOfAllFriends = []
    for i in listsOfAllFriends:
        setsOfAllFriends.append(set(i))
    for i in range(friends):
        marysSet = marysSet.difference(setsOfAllFriends[i])
    bro = list(marysSet)
    print(len(bro))
testCases = int(input())
for i in range(testCases):
    answer()

