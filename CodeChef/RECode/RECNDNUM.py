def walk(c):
    count = {}
    for k in range(1, c+1):
        i = 0
        while i < k:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
            print(f"{i} ----", end="")
            i += 1
        while i > 0:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
            print(f"{i} ----", end="")
            i -= 1
    print(count)


walk(3)
