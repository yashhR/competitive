s = "PAYPALISHIRING"
numRows = 3
def convert(s: str, numRows: int) -> str:
    rows = [[] for i in range(numRows)]
    ans = ''
    # [0, 1, 2, 1]
    kindex = []
    for i in range(numRows):
        kindex.append(i)
    for i in range(numRows-2, 0, -1):
        kindex.append(i)
    print(kindex)
    for i, c in enumerate(s):
        k = kindex[i % len(kindex)]
        print(f"for {i, c} k is {k}")
        rows[k].append(c)
    for i in range(len(rows)):
        print(rows[i])
        ans += ''.join(rows[i])
    return ans

print(convert(s, numRows))
'''
paypal in 3 rows
0, p, so 0%4 = 0, what's in 0th index of kindex, 0, so 0th row
1, a, so 1%4 = 1, what's in 1th index of kindex, 1, so 1th row
2, y, so 2%4 = 2, what's in 2th index of kindex, 2, so 2th row
3, p, so 3%4 = 3, what's in 3th index of kindex, 1, so 1th row
4, a, so 4%4 = 0, what's in 0th index of kindex, 0, so 0th row
5, l, so 5%4 = 1, what's in 1th index of kindex, 1, so 1th row

[p, a]
[a, p, l]
[y]
paaply
'''

'''
more clever approach (from leetcode solution blog):
'''

"""
def convert(self, s, numRows):
    :type s: str
    :type numRows: int
    :rtype: str
    lin = 0
    pl = 1
    outp = [""] * numRows
    for i in range(len(s)):
        outp[lin] += s[i]
        if numRows > 1:
            lin += pl
            if lin == 0 or lin == numRows - 1:
                pl *= -1
    outputStr = ""
    for j in range(numRows):
        outputStr += outp[j]
    return outputStr
"""