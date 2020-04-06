n, k = map(int, input().split())
seen = set()
minimum = n
if n % k == 0:
    print(0)
else:
    while True:
        if n in seen:
            print(minimum)
            break
        else:
            minimum = min(minimum, n)
            seen.add(n)
        n = abs(n-k)