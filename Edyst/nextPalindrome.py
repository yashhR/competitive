def next_palindrome(n):
    indigits = []
    for i in str(n):
        indigits.append(i)
    #isEven = 0
    digits = len(indigits)
    #if digits%2 == 0:
    #    isEven = 1
    #if isEven:
    #else:
    middle = indigits[digits//2]
    i = digits//2

    for j in range(1, (digits-1)//2 + 1):
        indigits[i+j] = indigits[i-j]
    possible = int(''.join(indigits))
    if possible > num:
        return possible
    else:
        if middle!='9':
            indigits[i] = f"{int(middle) + 1}"
            pos1 = int(''.join(indigits))
            return next_palindrome(pos1)

num = 128
print(next_palindrome(num))
