'''
arr = [4, 2, 5, 7]
flag = 0
idx = -1
for i in range(1, len(arr)):
    if flag:
        break
    else:
        if arr[:i] == sorted(arr[:i]):
            if arr[i+1:] == sorted(arr[i+1:]):
                flag = 1
                idx = arr[i]
                break

print(idx)
'''

orgList = [4, 2, 5, 7]
sortedList = sorted(orgList)
for i in range(1, len(orgList)):
    for i in arr[]