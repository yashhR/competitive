class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        def andOperator(a, b):
            while(a < b):
                b -= (b & -b)
            return b
        return andOperator(m, n)