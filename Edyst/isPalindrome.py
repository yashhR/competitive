def isPalindrome(A):
    main = ''
    for i in A:
        if i.isalnum():
            main += i.lower()
    print(main)
    if main[::-1] == main:
        return 1
    else:
        return 0

print(isPalindrome("A man, a plan, a canal: Panama"))