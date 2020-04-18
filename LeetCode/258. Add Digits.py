
# def addDigits(num: int) -> int:
#     def sum_digits(n):
#         sumi = 0
#         for digit in str(n):
#             sumi += int(digit)
#         return sumi
#     while len(str(num)) > 1:
#         num = sum_digits(num)
#     return num


def add_digits(num):
    if len(str(num)) > 1:
        sumi = 0
        for c in str(num):
            sumi += int(c)
        return add_digits(sumi)
    else:
        return num


print(add_digits(38))