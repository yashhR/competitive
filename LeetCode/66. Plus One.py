def plus_one(digits):
    if digits[-1] != 9:
        digits[-1] += 1
    else:
        if len(digits) == 1:
            digits[0] = 0
            digits.insert(0, 1)
        else:
            digits[-1] = 0
            digits[-2] += 1
            i = len(digits) - 2
            while digits[i] == 10:
                print(digits)
                if i == 0:
                    digits[i] = 0
                    digits.insert(0, 1)
                    break
                digits[i] = 0
                digits[i-1] += 1
                i -= 1
    return digits


print(plus_one([9, 9]))
