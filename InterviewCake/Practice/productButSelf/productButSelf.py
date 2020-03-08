'''
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Here's the catch: You can't use division in your solution!


Solution Approach:
I have seen Nick White solve the exact same problem, so I used the same approach!
'''


def get_products_of_all_ints_except_at_index(int_list):
    # Make a list with the products
    n = len(int_list)
    if n == 0 or n == 1:
        raise AssertionError
    else:
        lefts = {0: 1}
        rights = {n-1: 1}
        for i in range(1, n):
            lefts[i] = int_list[i-1]*lefts[i-1]
        for i in range(n-2, -1, -1):
            rights[i] = int_list[i+1]*rights[i+1]
        ans = []
        for i in range(n):
            ans.append(lefts[i]*rights[i])
        return ans
