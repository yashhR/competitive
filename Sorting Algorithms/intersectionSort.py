'''
Insertion sort can sort the list as it receives it

You basically start from the second element in the array, and you check for everything before it,
move everything to the right by one place and replace our element in the correct position
'''

arr = list(map(int, input().split()))
for i in range(1, len(arr)):
    v = arr[i]
    j = i
    print(v)
    while arr[j-1] > v and j > 0:
        arr[j] = arr[j-1]
        j -= 1
    arr[j] = v

print(arr)
