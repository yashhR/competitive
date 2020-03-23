'''
Given a 32-bit signed integer, reverse digits of an integer.
'''


class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        ans = 0
        i = len(s) - 1
        if s[0] == '-':
            while i > 0:
                ans -= int(s[i])*(10**(i-1))
                i -= 1
        else:
            while i > -1:
                ans += int(s[i])*(10**i)
                i -= 1
        if not (2**31-1) >= ans >= (-2**31):
            return 0
        return ans