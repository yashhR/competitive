'''
Given a positive integer, output its complement number.
The complement strategy is to flip the bits of its binary representation.



Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits),
and its complement is 010. So you need to output 2.


Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0.
'''


def findComplement(num: int) -> int:
    def dec_to_bin(n):
        return bin(n).replace("0b", "")
    ret = dec_to_bin(num)
    print(ret)
    ans = 0
    factor = 1
    for c in ret[::-1]:
        ans += (1 - int(c)) * factor
        factor = factor*2
    return ans

print(findComplement(2))