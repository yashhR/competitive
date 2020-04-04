'''
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


# def move_zeroes(nums):
#     while True:
#         swaps = 0
#         for i in range(len(nums)-1):
#             if nums[i] == 0 and nums[i+1] != 0:
#                 swaps += 1
#                 nums[i], nums[i+1] = nums[i+1], nums[i]
#         if swaps == 0:
#             break
#     return nums
#
#
# print(move_zeroes([0, 0, 0, 0, 0]))
# This solution did better than 5% of all python solution, meaning that this is one of the worst solutions there is.
# Ran in 1476 ms


# def move_zeroes(nums):
#     i = 0
#     totalZeroes = len(nums)
#     while i < len(nums):
#         if nums[i] == 0:
#             bro = i
#             noOfConsecZeroes = 0
#             while bro < len(nums) and nums[bro] == 0:
#                 noOfConsecZeroes += 1
#                 bro += 1
#             idx = i
#             swaps = 0
#             while idx < len(nums) - noOfConsecZeroes:
#                 swaps += 1
#                 nums[idx] = nums[idx+noOfConsecZeroes]
#                 idx += 1
#             while idx < len(nums):
#                 nums[idx] = 0
#                 idx += 1
#             if swaps == 0:
#                 break
#             i += noOfConsecZeroes
#         else:
#             noOfConsecZeroes = 0
#             i += 1
#     return nums
#
#
# print(move_zeroes([0, 1, 0, 0, 1]))
# Even this solution did better than only 5% of all python solutions
# Ran in 952 ms


# def moveZeroes(nums):
#     count = 0
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             count += 1
#     nums[:] = [x for x in nums if x != 0]
#     nums.extend([0] * count)
# This does better than 55% of all python solutions


# def move_zeroes(nums):
#     idx = 0
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[idx] = 0
#             idx += 1
#     for i in range(idx, len(nums)):
#         nums[idx] = 0
#     return nums
# This does better than 97.4% of all python solutions
