t = int(input())
for _ in range(t):
    size = int(input())
    s = list(input())
    days = int(input())
    people_to_be_isolated = list(map(int, input().split()))
    isolated_people = set()
    positions = {}
    already_done = set()
    while days > 0:
        isolated_people.add(people_to_be_isolated.pop(0))
        for i in range(len(s)):
            if s[i] == '1':
                if i not in positions:
                    if i not in already_done:
                        positions[i] = True
                else:
                    already_done.add(i)
                    del positions[i]
        for position in positions.keys():
            if position + 1 not in isolated_people:
                if position == len(s) - 1:
                    s[position-1] = '1'
                else:
                    s[position-1] = '1'
                    if position + 2 not in isolated_people:
                        s[position+1] = '1'
            else:
                if position != len(s) - 1:
                    if position + 2 not in isolated_people:
                        s[position+1] = '1'
        print(''.join(s))
        days -= 1
    count = 0
    for i in range(len(s)):
        if s[i] == '1':
            count += 1
    print(count)