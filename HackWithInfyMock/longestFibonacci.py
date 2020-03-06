from itertools import combinations
arr = list(map(int, input().split(",")))
arr.sort()
n = len(arr)
def ans():
    def satisfies(a):
        flag = 0
        for i in range(2, len(a)):
            if a[i] == a[i-1] + a[i-2]:
                flag = 1
            else:
                flag = 0
                break
        if flag:
            return True
        return False
    flag = 0
    for i in range(n, 3, -1):
        combs = list(combinations(arr, i))
        for each in combs:
            if satisfies(list(each)):
                flag = 1
                return list(each)
    if not flag:
        return -1
x = ans()
for i in range(len(x)):
    if i == len(x)-1:
        print(x[i])
    else:
        print(x[i], end=",")