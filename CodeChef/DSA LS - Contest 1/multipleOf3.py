t = int(input())
for _ in range(t):
    k, d0, d1 = map(int, input().split())
    c = 2
    sumi = d0 + d1
    if k <= 11:
        while c < k:
            sumi += sumi % 10
            c += 1
        if sumi % 3 == 0:
            print("YES")
        else:
            print("NO")
    else:
        repeat = ''
        while c < 7:
            bitch = sumi % 10
            sumi += bitch
            repeat += str(bitch)
            c += 1
        number = str(d0) + str(d1) + repeat
        repeat = number[-4:].split()
        q = (k - 3 // 4)
        print(q)
        diff = 4*(q+1) - k
        print(diff)
        last_add = repeat[:-diff]
        print(last_add)

'''
11, 3, 4
c = 2
sum = 3 + 4 = 7 
sum = 7 + 7%10 = 7 + 7 = 14
c = 3
sum = 14 + 14%10 = 14 + 4 = 18
c = 4
sum = 18 + 18%10 = 18 + 8 = 26
c = 5
sum = 26 + 26%10 = 26 + 6 = 32
c = 6
sum = 32 + 32%10 = 32 + 2 = 34
c = 7
sum = 34 + 34%10 = 34 + 4 = 38
c = 8
sum = 38 + 38%10 = 38 + 8 = 46
c = 9
sum = 46 + 46%10 = 46 + 6 = 52
c = 10
sum = 52 + 52%10 = 52 + 2 = 54 
'''