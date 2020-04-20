# t = int(input())
# mod = 10**9 + 7
# for _ in range(t):
#     n, a = map(int, input().split())
#     i = 1
#     num = a
#     while n:
#         if n == 1:
#             num = num**i
#             num = num % mod
#             i += 2
#             n -= 1
#         else:
#             # print(num, factor[i])
#             num = num*(num**i)
#             num = num % mod
#             i += 2
#             n -= 1
#             # print(num)
#     print(num % mod)

t = int(input())
mod = 10**9 + 7
for _ in range(t):
    n, a = map(int, input().split())
    ans = (a**((n**2)-1))**(2*n-1)
    print(ans % mod)