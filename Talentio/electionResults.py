'''
5
4
192
48
206
37
147
90
312
21
186
12
121
38
114
21
408
39
267
13
382
29
Output: C has won


5
4
192
148
206
37
147
190
312
21
186
312
121
38
114
121
408
39
267
113
382
29
Output: Runoff between A and C
'''

booths = int(input())
candidates = int(input())
matrix = [[0 for i in range(candidates)] for i in range(booths)]
dict = {0:'A', 1:'B', 2:'C', 3:'D'}
total = 0
candVotes = []
for i in range(booths):
    for j in range(candidates):
        matrix[i][j] = int(input())
        total += matrix[i][j]

print(total)
for j in range(candidates):
    votes = 0
    for i in range(booths):
        votes += matrix[i][j]
    candVotes.append(votes)

print(candVotes)

flag = 0
for i in range(len(candVotes)):
    if candVotes[i] > total/2:
        flag = 1
        indexOfWinner = i
if flag:
    print(f"{dict[indexOfWinner]} has won!")
else:
    highest = max(candVotes)
    i = candVotes.index(highest)
    candVotes[i] = 0
    secondHighest = max(candVotes)
    j = candVotes.index(secondHighest)
    print(f"Runoff between {dict[j]} and {dict[i]}")






