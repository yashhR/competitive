t = int(input())
def solve(n):
    divisors = []
    for k in range(1, n):
        if n%k == 0:
            divisors.append(k)
    if sum(divisors) == n:
        return "YES"
    return "NO"


for i in range(t):
    N = int(input())
    print(solve(N))