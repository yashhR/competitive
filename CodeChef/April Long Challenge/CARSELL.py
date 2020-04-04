t = int(input())
for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))
    prices.sort()
    profit = 0
    done = False
    bro = False
    for i in range(len(prices)):
        if prices[i] != 0:
            bro = True
            profit += prices[i]
        if bro:
            for j in range(i + 1, len(prices)):
                prices[j] -= 1
        if sum(prices) == 0:
            done = True
            print(profit)
            break
    if not done:
        print(profit % 1000000007)
