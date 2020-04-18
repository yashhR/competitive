
def isUgly(num: int) -> bool:
    if num == 1:
        return True
    while num % 2 == 0:
        print(num)
        num = num // 2
    for i in range(3, 6, 2):
        while num % i == 0:
            print(num, i)
            num = num // i
    print(num)
    if num == 1:
        return True
    return False


print(isUgly(8))


