testCases = int(input())

def min_hours():
    fairPoint = None
    flag = 0
    totalStudents, pickStudents = map(int, input().split(" "))
    skills = list(map(int, input().split(" ")))
    for i in skills:
        if skills.count(i) > 1:
            flag = 1
            fairPoint = i
            break
    if not flag:
        avg = sum(skills) // totalStudents
        min = 1000000000
        for i in skills:
            if abs(avg - i) <= min:
                min = abs(avg - i)
                fairPoint = i
    tr = []
    for i in skills:
        tr.append(abs(fairPoint - i))
    tr.sort()
    print(tr)
    return sum(tr[:pickStudents])

for i in range(testCases):
    k = min_hours()
    print(f"Case #{i+1}: {k}")
