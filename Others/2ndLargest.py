'''
# 5, 7, 2, 6, 4
arr = list(map(int, input().split()))


def sort_karo(a):
    idx = 0
    count = 0
    for j in range(len(a)):
        flag = 0
        mini = a[j]
        for i in range(j, len(a)):
            if a[i] <= mini:
                flag = 1
                mini = a[i]
                idx = i
        if flag:
            count += 1
            a[j], a[idx] = a[idx], a[j]
        if is_sorted(a):
            break
    print(count)
    return a


def is_sorted(a):
    for i in range(len(a)-1):
        if a[i+1] >= a[i]:
            continue
        else:
            return False
    return True

arr = sort_karo(arr)

print(arr)

'''

arr = list(map(int, input().split()))