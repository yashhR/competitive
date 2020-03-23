def longestPalindrome(s: str) -> str:
    def isPalindrome(arg):
        if arg == arg[::-1]:
            return True
        return False
    allPals = ['']
    if isPalindrome(s):
        return s
    for i in range(len(s)):
        for j in range(len(s), i+len(allPals[-1]), -1):
            lol = s[i:j]
            if isPalindrome(lol) and len(lol) > len(allPals[-1]):
                allPals.append(lol)
                break
    return allPals[-1]


print(longestPalindrome("cbbd"))

'''
This got accepted but only did better than 30% of all Python solutions
It did better than 100% of all python solutions in terms of memory
'''