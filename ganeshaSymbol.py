n = int(input())
for i in range(n):
    if i <= n//2:
        if i == 0:
            print("*", end="")
            t = (n - 3) // 2
            while t:
                print(" ", end="")
                t -= 1
            t = 2 + (n-3)//2
            while t:
                print("*", end="")
                t -= 1
            
        elif i == n//2:
            t = n
            while t:
                print("*", end="")
                t -= 1
        else:
            print("*", end="")
            t = (n-3) // 2
            while t:
                print(" ", end="")
                t -= 1
            print("*")
    else:
        if i == n-1:
            t = 2 + (n-3)//2
            while t:
                print("*", end="")
                t -= 1
            t = (n - 3) // 2
            while t:
                print(" ", end="")
                t -= 1
            print("*", end="")
        else:
            t = (n-3) // 2
            while t:
                print(" ", end="")
                t -= 1
            print("*", end="")
            t = (n-3) // 2
            while t:
                print(" ", end="")
                t -= 1
            print("*")