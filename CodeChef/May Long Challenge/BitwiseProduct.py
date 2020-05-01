t = int(input())
while t:
    x, y, l, r = map(int, input().split())
    maxi = -1
    for num in range(l, r+1):
        temp = (x & num)*(y & num)
        print(temp, num)
        if temp > maxi:
            maxi = temp
            ans = num
    print(maxi, ans)
    # if x == y and l <= x <= r:
    #     print(x)
    # else:
    #     if x < y:
    #         if x <= 15:
    #             print(15)
    #         elif x < 155:
    #             print()
    #     else:

    t -= 1