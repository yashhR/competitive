s = input()
start = (0, 0)
seen = set()
seen.add(start)
falls = 0
for c in s:
    if c == 'L':
        start = (start[0], start[1] - 1)
    elif c == 'R':
        start = (start[0], start[1] + 1)
    elif c == 'U':
        start = (start[0]-1, start[1])
    elif c == 'D':
        start = (start[0]+1, start[1])
    if start in seen:
        falls += 1
    else:
        seen.add(start)
print(falls)
