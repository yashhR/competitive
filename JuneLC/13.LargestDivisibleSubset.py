"""
Given a set of distinct positive integers,
find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
"""

def LDS(nums):
    """
    1. my idea is to first sort the nums array
    2. And maintain an aux array that contains each possibility of the answer
    3. We start with the first element and keep adding the element that can be divided by the prev ele in aux array
    4. We recurse and keep track of the length of the aux array
    5. As we do this for all possible aux arrays, we also maintain the max seen
    6. And then we return the largest aux array seen
    """

     
    n = len(nums)
    counts = [1 for x in nums]
    maxC = -1
    maxidx = 0
    for i in range(n):
        for j in range(i-1, -1, -1):
            if nums[i] % nums[j] == 0:
                counts[i] = max(counts[i], counts[j] + 1)
                if counts[i] > maxC:
                    maxC = counts[i]
                    maxidx = i
    res = []
    temp = nums[maxidx]
    currCount = counts[maxidx]
    for i in range(maxidx, -1, -1):
        if temp % nums[i] == 0 and counts[i] == currCount:
            res.append(nums[i])
            temp = nums[i]
            currCount -= 1
    return res


print(LDS([1, 4, 5, 8, 9, 12]))