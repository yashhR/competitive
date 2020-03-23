'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        res = ""
        i = 0
        lengths = []
        for l in range(len(strs)):
            lengths.append(len(strs[l]))
        while i < min(lengths):
            first = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] == first:
                    flag = 1
                else:
                    return res
            if flag:
                res += first
                i += 1

        return res
