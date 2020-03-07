'''
This was asked in an Amazon interview:

You are given an array of numbers and are asked to start deleting numbers from the end of array.

Every time you delete a number, you must tell the maximum element of the modified array after deletion in O(1).

Example Input:
2 6 3 4 5

Output:
6 6 6 6 2


The solution was inspired by a method that YouTuber Nick White used to solve the MinStack question (LeetCode 155)
'''


def MaxElementFromEnd(Arr):
    bro = sorted(Arr)                             # Create an array that has the original array sorted
    res = [bro[-1]]                               # append the maximum element of og array before deletion
    for i in range(len(Arr)-1):                   # pop the last element in the og array as asked
        l = Arr.pop()                             # delete the same element from the sorted list,
        bro.remove(l)                             # now, in bro, whatever elements are left in og array are sorted
        res.append(bro[-1])                       # simply, the last element of bro list is the max of whats left
    return res


print(MaxElementFromEnd([2, 6, 3, 4, 5]))