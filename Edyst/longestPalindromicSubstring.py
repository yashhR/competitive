def longestPalindrome(A):
    def is_palindrome(x):
        if x == x[::-1]:
            return True
        return False
    if is_palindrome(A):
        return A
    allSubs = ['']
    for i in range(len(A)):
        for j in range(i + len(allSubs[-1]), len(A)):
            if is_palindrome(A[i:j + 1]) and len(A[i:j + 1]) > len(allSubs[-1]):
                allSubs.append(A[i:j + 1])
    print(allSubs)
    return allSubs[-1]

print(longestPalindrome("aaaabaaa"))

