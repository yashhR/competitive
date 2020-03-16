'''
Very suprisingly, just a week ago, I wondered if in my interview, I was asked to sort the array
manually instead of using the python sort function, what would I do? and wrote my own sorting algorithm.
Now that I am preparing the well known ones, I realized that my sorting algorithm is the exact SAME as SELECTION SORT.

For every element, you check the array on the right of it and find the minimum of the rest of the array and
swap with the element in place.
'''

arr = list(map(int, input().split()))
for i in range(len(arr)):
    mini = arr[i]
    for j in range(i, len(arr)):
        if arr[j] <= mini:
            mini = arr[j]
            idx = j
    arr[i], arr[idx] = arr[idx], arr[i]

print(arr)
