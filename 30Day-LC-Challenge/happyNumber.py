'''
Happy Number
Solution
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''


def is_happy(n):
    def sum_of_squares(num):
        sumi = 0
        s = str(num)
        for i in range(len(s)):
            sumi += int(s[i])**2
        return sumi
    seen = set()
    while True:
        lol = sum_of_squares(n)
        if lol == 1:
            return True
        else:
            if lol in seen:
                return False
            seen.add(lol)
            n = lol


print(is_happy(20))
# This solution got accepted and it did better than 99.38% of all python solutions.

'''
This is the best solution using O(1) space
If you remember the solution of finding the cycle in linked-list, you can use same method : "Catch up!"

def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    r1 = self.step(n)
    r2 = self.step(r1)
    while(r1 != 1):
        if(r1 == r2):
            return False
        else:
            r1 = self.step(r1)
            r2 = self.step(self.step(r2))
    return True

def step(self, n):
    result = 0
    while(n):
        result += pow(n % 10, 2)
        n = n // 10
    return result
'''