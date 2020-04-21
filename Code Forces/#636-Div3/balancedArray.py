t = int(input())
for _ in range(t):
    n = int(input())
    if n//2 % 2:
        print("NO")
    else:
        print("YES")
        result = []
        haha = 2
        m = n // 2
        while m:
            result.append(haha)
            haha += 2
            m -= 1
        m = n // 2
        haha = 1
        sumi = 0
        while m - 1:
            result.append(haha)
            sumi += haha
            haha += 2
            m -= 1
        result.append(n//2*(n//2+1) - sumi)
        for i in range(len(result)):
            if i == len(result) - 1:
                print(result[i])
            else:
                print(result[i], end=" ")