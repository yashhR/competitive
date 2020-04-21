t = int(input())
for _ in range(t):
    n = int(input())
    sumi = 3
    k = 3
    while True:
        if sumi > n:
            break
        else:
            if n % sumi == 0 and k > 1:
                print(n // sumi)
                break
            else:
                sumi += 2**(k-1)
                k += 1