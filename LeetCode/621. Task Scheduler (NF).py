def task_scheduler(tasks, n):
    cpu = []
    uniques = []
    seen = {}
    for task in tasks:
        if task not in seen:
            seen[task] = 1
            uniques.append(task)
        else:
            seen[task] += 1
    # print(seen)
    while len(uniques):
        b = len(uniques)
        # print(f"Uniques are {uniques}, length is {b}")
        for unique in uniques:
            cpu.append(unique)
            seen[unique] -= 1
        delthese = []
        for key in seen:
            if seen[key] == 0:
                delthese.append(key)
                uniques.remove(key)
        for key in delthese:
            del[key]
        if len(uniques):
            while n - b + 1:
                cpu.append("idle")
                b += 1
    # print(cpu)
    return len(cpu)


print(task_scheduler(["A", "A", "A", "B", "B", "B"], 2))





'''
n = 2
AABBCCDDEEFFGGHH

ABCDEFGHABCDEFGH

if n > uniqueChars:
    n + (n - uniqueChars)
elif n < uniqueChars:
    len(tasks)
elif n == uniqueChars:

2
'''