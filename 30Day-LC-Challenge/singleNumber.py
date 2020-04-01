'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

# arr = list(map(int, input().split()))
# arr.sort()
#
# found = False
# i = 0
# while i < len(arr) - 1:
#     if arr[i] != arr[i+1]:
#         found = True
#         print(arr[i])
#         break
#     else:
#         i += 2
#
#
# if not found:
#     print(arr[-1])
# The above solution runs in O(N*logN) time complexity because NlogN to sort and N/2 to go through the sorted array
# We were asked to write a linear time solution
# Bitch, guess what! This solution got accepted as well and it did better than 98.9% of all python solutions.
# I was not expecting this at all


# arr = list(map(int, input().split()))
# hashSet = set()
#
# for i in range(len(arr)):
#     if arr[i] not in hashSet:
#         hashSet.add(arr[i])
#     else:
#         hashSet.discard(arr[i])
#
# for item in hashSet:
#     print(item)
# The above solution is O(N) time complexity because we loop through the array once. But with O(N) space complexity
# We were asked to write a linear time solution without extra space
# This solution got accepted and passed all 16 test cases
# The runtime beats 65.17% of all python solutions.


# arr = list(map(int, input().split()))
# seen = set()
#
# for i in range(len(arr)):
#     if arr[i] not in seen:
#         seen.add(arr[i])
#     else:
#         arr[i] = -(arr[i])
#
# ans = 0
# for i in range(len(arr)):
#     ans += arr[i]
#
# print(ans)

# ---------------------------------------------------------------------------------------------------------------------

# Best solution using XOR. Takes O(n) time complexity and NO extra space

arr = list(map(int, input().split()))

result = 0

for num in arr:
    result ^= num

print(result)

'''
The way this works is based around the property of XOR.
A XOR of a value with itself is 0.
So, for every pair in the array, the XOR of it with itself with result in 0 except for the element occuring just once.

So, finally, 0^singleNumber = singleNumber

and we return it. LOL!

I had the thought of making everything else zero except for the single element, which is what I did in the third sol.
If it is in the seen set, then change its value to negative of itself and, after one complete iteration,
just sum all the elements and because all the pairs have become zero, the sum will be equal to the solo element.

XOR is basically doing just that without any extra space to check if it is already seen and doesn't require another 
loop to get the sum of the elements. SO FREAKING COOL.
'''