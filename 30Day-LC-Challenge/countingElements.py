'''
Given an integer array arr, count element x such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.

Example 1:
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.


Example 2:
Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there's no 2, 4, 6, or 8 in arr.


Example 3:
Input: arr = [1,3,2,3,5,0]
Output: 3
Explanation: 0, 1 and 2 are counted cause 1, 2 and 3 are in arr.


Example 4:
Input: arr = [1,1,2,2]
Output: 2
Explanation: Two 1s are counted cause 2 is in arr.


Constraints:
1 <= arr.length <= 1000
0 <= arr[i] <= 1000
'''


# def countElements(arr):
#     freq = {}
#     count = 0
#     for num in arr:
#         if num in freq:
#             freq[num] += 1
#         else:
#             freq[num] = 1
#     for num in freq.keys():
#         if num + 1 in freq.keys():
#             count += freq[num]
#     return count
#
#
# print(countElements([1, 2, 3]))
# This runs in 40ms


def count_elements(arr):
    arr.sort()
    i = 0
    count = 0
    while i < len(arr):
        bitch = arr[i]
        freq = 0
        while i < len(arr) and arr[i] == bitch:
            i += 1
            freq += 1
        if i < len(arr) and arr[i] == bitch + 1:
            count += freq
    return count


print(count_elements([1, 3, 2, 3, 5, 0]))
# This runs in 72ms
