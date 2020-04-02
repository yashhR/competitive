from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    teamA = list(map(int, stdin.readline().split(" ")))
    teamB = list(map(int, stdin.readline().split(" ")))
    maxA = max(teamA)
    found = False
    for speed in teamB:
        if speed > maxA:
            found = True
            print("YES")
            break
    if not found:
        print("NO")
