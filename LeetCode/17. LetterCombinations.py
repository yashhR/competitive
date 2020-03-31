'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''



'''
Pythonic approach to this problem would be to import the product function from the itertools module
The product function does the cartesian product of the lists passed as arguments to it, 
but this returns a tuple , so you will have to join the elements in the tuple to form a string and then return

This did well better than ONLY 25% of the total python solutions, so you will be asked to kindly fuck off from
the interview if you can't come up with a better solution
'''
# from itertools import product
#
# def letterCombinations(digits: str):
#     maps = {
#         '2': ['a', 'b', 'c'],
#         '3': ['d', 'e', 'f'],
#         '4': ['g', 'h', 'i'],
#         '5': ['j', 'k', 'l'],
#         '6': ['m', 'n', 'o'],
#         '7': ['p', 'q', 'r', 's'],
#         '8': ['t', 'u', 'v'],
#         '9': ['w', 'x', 'y', 'z']
#     }
#     returnval = ''
#     # for num in range(len(digits)):
#     #     for char in range(len(digits[num]))
#     lists = []
#     for num in digits:
#         lists.append(maps[num])
#
#     result = list(product(*lists))
#     for i in range(len(result)):
#         result[i] = (''.join(result[i]))
#     return result


'''
This was my second thought, what if the interviewer was kind enough and asked me to implement the product function
on my own instead of importing.
So, I thought to implement it.
Suppose there are two lists and you are supposed to return the product of both of them, what you gotta do is,
for each element in the first list, you have to append each element in the second list and the result should be appended
to the return list.

This is the base case, you will be given more than 2 numbers, that means, the product should be done among multipleLists

for multiple lists, if we observe, this multiplication happens from the behind, in the sense that - the last two lists
are multiplied first, the result is stored and this is now multiplied with the before list, now again res is stored
and multiplied with the before list.

So, what we can do is, store the value of prev multiplication and from behind we can keep multiplying and updating the
prev value with all the lists until the beginning, in the end the value in prev will be our answer!

This did better than 66% of all the python solutions, you may still have to optimize the solution 
'''


def letterCombinations(digits: str):
    maps = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    if digits == '':
        return []
    prev = maps[digits[-1]]

    def product(lis1, lis2):
        result = []
        for each in lis1:
            for eah in lis2:
                result.append(each+eah)
        return result
    i = len(digits)-2
    while i > -1:
        prev = product(maps[digits[i]], prev)
        i -= 1
    return prev


print(letterCombinations("23"))