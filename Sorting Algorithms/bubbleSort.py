'''
Go through the elements from the beginning to the ending,
and compare every two consecutive elements, and swap them in a way that the larger element
moves to the end of the list
[9, 7, 12, 69, 1, 10, 42]
[7, 9, 12, 69, 1, 10, 42]
[7, 9, 12, 1, 69, 10, 42]
[7, 9, 1, 12, 10, 69, 42]
[7, 1, 9, 10, 12, 42, 69]

As you can see, after one complete iteration, the largest element of the array goes to the last place
'''

arr = list(map(int, input().split()))
count = 0
for i in range(len(arr)):
    count += 1
    swap = 0
    for idx in range(len(arr)-1-i):
        if arr[idx] > arr[idx + 1]:
            swap += 1
            arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
    print(arr)
    if swap == 0:
        print(arr)
        break
print(count)

'''
After every pass, it is guarantted that the largest element moves to the end of the list, 
which means you don't have to check until the last element (check as in compare)
so, for every pass, you only have to iterate through the list until the end minus the number of times you
have already looped before, which indicates the number of elements that are already sorted at the end.

The only good thing about bubble sort is that we can use it as a flag to check whether the given 
array is already sorted or NOT.

this can be added as an additional check after every pass, that if there are NO SWAPS, then it means that
the array is already sorted, so you can just print the array and break out of the loop.
'''
