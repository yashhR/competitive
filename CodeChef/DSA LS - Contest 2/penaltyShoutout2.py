t = int(input())
for _ in range(t):
    n = int(input())
    shots = input()
    a = 0
    b = 0
    gotAnswer = False
    for i in range(len(shots)):
        if i % 2 == 0:
            a += int(shots[i])
            if i >= n:
                if a > b:
                    if a - b > b + n - ((i+2)//2) + 1:
                        print(i+1)
                        gotAnswer = True
                        break
                elif b > a:
                    if b - a > a + n - ((i+2)//2):
                        print(i+1)
                        gotAnswer = True
                        break
        else:
            b += int(shots[i])
            if i >= n:
                if a > b:
                    if a - b > b + n - ((i+1)//2):
                        print(i+1)
                        gotAnswer = True
                        break
                elif b > a:
                    if b - a > a + n - ((i+1)//2):
                        print(i+1)
                        gotAnswer = True
                        break
    if not gotAnswer:
        print(2*n)
