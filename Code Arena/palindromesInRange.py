'''
Given two numbers a and b, return the count of number of palindromes within that range
10, 13 -- 10, 11, 12, 13 -- 11 is the only palidrome, so return 1
1, 9 -- all of them are palindromes, so return 9
'''

# Brute force approach


# def solution(a, b):
#     count = 0
#
#     def is_palindrome(number):
#         if str(number) == str(number)[::-1]:
#             return True
#         return False
#     for num in range(a, b+1):
#         if is_palindrome(num):
#             count += 1
#
#     return count


# But the above solution is bad it checks if every number in the range is a palindrome, even though we know it doesn't
# have to, in the sense that, if we know that 121 is a palindrome we dont have to check for 122, 123, ... 130,
# the next palindrome will occur at 131 and we know that. So we can skip.


def solution(a, b):
    count = 0
    '''
    1 - 10 = 9
    10 - 100 = 9
    100 - 200 = 9
    200 - 300 = 9
    300 - 400 = 9
    ..
    ..
    ..
    ..
    ..
    800 - 900: 9
    900 - 1000: 9
    1001 - 2000: 1001, 1111, 1221, 1331, 1441, 1551, 1661, 1771, 1881, 1991: 10
    2001 - 3000: 2002, 2112, 2222, 2332, 2442, 2552, 2662, 2772, 2882, 2992: 10
    .
    .
    9001 - 10000: 9009, 9119, 9229, 9339, 9449, 9559, 9669, 9779, 9889, 9999: 10
    '''

    def round_to_nearest(num):
        power = len(str(num)) - 1
        return (num//10**power) * 10**power

    print(round_to_nearest(a))
    print(round_to_nearest(b))


solution(11, 203)