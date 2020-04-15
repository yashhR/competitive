'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

'''
There's three ways to think about it 

1. Linear Search (O(n) time and O(1) space)
   This is very intuitive, all you got to do is, go through the list and when you find the target, set that as 
   the first occurence and from there on iter through the list looking for the index where its not equal to the
   target and return [first, last] last will be the index where its not equal - 1
   
   
2. Binary Search and then Linear search (O(n) time and O(1) space)
   This is uselessly smart, and what I mean by that is that the time complexity is the same even if you do Binary search
   What you do is you binary search for the element and from the position you go to left till its not equal, store it
   as first, go right till its not equal, store it as last
   
   
3. Binary search and binary search (O(logn) time and O(1) space)
   In the binary search function, you also provide the type of search you are doing, that is whether you are looking
   for the first occurence or the last occurence.
   
   For the first occurence, you dont return the index as soon as you find the value, you see if the index before the 
   present is in bounds and check if the value before is the same as the value as now, if it is, then it means that
   there are values to the left equal to target and then you do binary search on the range (start, mid - 1)
   
   For the second occurence, you do the same as above except that you check that the next element is in bounds & if the
   next element is the same as that of present's, it means that there are more values to the right that are equal to the
   target and then you recursively call the binary search on mid + 1 to the end with the same search type
   
   Any some point, either the index gounds out of bounds or the value wont be the same to the neightboring, 
   in that case you just return the index and store it in a variable acc to the search type and you return [first, last]
'''


def searchRange(nums, target):
    def binary_search(array, start, end, value, search_type):
        if start <= end:
            mid = end + (start-end)//2
            if array[mid] == value:
                if search_type == 0:
                    if mid - 1 >= 0 and array[mid-1] == array[mid]:
                        end = mid - 1
                        return binary_search(nums, start, end, value, search_type)
                if search_type == 1:
                    if mid + 1 <= n - 1 and array[mid+1] == array[mid]:
                        start = mid + 1
                        return binary_search(nums, start, end, value, search_type)
                return mid

            elif array[mid] > value:
                end = mid - 1
                return binary_search(array, start, end, value, search_type)
            elif array[mid] < value:
                start = mid + 1
                return binary_search(array, start, end, value, search_type)
        else:
            return -1
    n = len(nums)
    first = binary_search(nums, 0, n - 1, target, 0)
    if first == -1:
        return [-1, -1]
    else:
        last = binary_search(nums, 0, n - 1, target, 1)
        return [first, last]


print(searchRange([1], 1))
