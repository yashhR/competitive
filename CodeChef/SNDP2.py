t = int(input())
while t:
    n, m = map(int, input().split())
    elements = list(map(int, input().split()))
    greater, lesser, equal = 0, 0, 0
    seen = set()
    for each in elements:
        if each > m:
            greater += 1
        elif each < m:
            lesser += 1
        else:
            equal += 1
    if equal == n:
        print(-1)
    elif lesser == m - 1:
        print(lesser + greater)
    else:
        print(greater)
    t -= 1