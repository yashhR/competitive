n = int(input())
count = {}
while n:
    a, b = input().split(' ')
    if a in count:
        count[a] += 1
    else:
        count[a] = 1
    if b in count:
        count[b] += 1
    else:
        count[b] = 1
    n -= 1
okay = []
for key in count:
    okay.append((key, count[key]))
okay.sort(key = lambda x: x[1], reverse = True)
i = 0
highest = okay[0][1]
while okay[i][1] == highest:
    print(okay[i][0])
    i += 1