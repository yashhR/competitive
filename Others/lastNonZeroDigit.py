n = int(input())


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


fact = factorial(n)
factor = 5
trailing_zeroes = 0
while factor <= n:
    trailing_zeroes += n//factor
    factor *= 5
print(str(fact)[-trailing_zeroes-1])
