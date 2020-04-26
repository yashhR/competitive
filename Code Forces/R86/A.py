t = int(input())
while t:
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    if x == y:
        if 2*a >= b:
            print(b*x)
        else:
            print(2*a*x)
    else:
        if 2*a >= b:
            if x > y:
                print(b*y + a*(x-y))
            else:
                print(b*x + a*(y-x))
        else:
            if x > y:
                print(2*a*y + a*(x-y))
            else:
                print(2*a*x + a*(y-x))
    t -= 1