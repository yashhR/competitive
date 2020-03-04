


str = list(map(int, input().split()))
minlist = []
mini = abs(str[0]) + abs(str[1])
for i in range(0, len(str)-1, 2):
    if abs(str[i]) + abs(str[i+1]) < mini:
        mini = abs(str[i])+abs(str[i+1])

for i in range(0, len(str)-1, 2):
    if abs(str[i])+abs(str[i+1]) == mini:
        print(f"({str[i]},{str[i+1]})")

## test case = -4,5|-5,5|-1,-2|-2,-1|1,2|2,1|-7,-3|-6,6
