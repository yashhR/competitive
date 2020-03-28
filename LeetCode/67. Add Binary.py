'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

'''
Just like you would do in a decimal addition when doing manually, you add up the stuff at the right most 
(least significant) and just keep doing that moving towards the left, (most significant) - and everytime, you add
you see if there's a carry and then you just add it to the next add operation you do.
'''

# SOLUTION 1

# def add_binary(a, b):
#     carry = 0
#     i = len(a) - 1
#     j = len(b) - 1
#     retval = ''
#     while i >= 0 or j >= 0:
#         summation = carry
#         if i >= 0:
#             summation += int(a[i])
#         if j >= 0:
#             summation += int(b[j])
#         retval = str(summation % 2) + retval
#         carry = summation//2
#         i -= 1
#         j -= 1
#     if carry:
#         retval = str(carry) + retval
#     return retval


# SOLUTION 2


# def add_binary(a, b):
#     def convert(a):
#         # i = len(a) - 1
#         factor = 1
#         summation = 0
#         for i in range(len(a)-1, -1, -1):
#             summation += int(a[i])*factor
#             print(i, int(a[i]), factor, summation)
#             factor *= 2
#         return summation
#     aDEC = convert(a)
#     bDEC = convert(b)
#     addition = aDEC + bDEC
#     retval = ''
#     while addition > 0:
#         retval = str(addition % 2) + retval
#         addition = addition // 2
#     return retval


# print(add_binary("1010", "1011"))
