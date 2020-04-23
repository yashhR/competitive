t = int(input())
while t:
    n, k = map(int, input().split())
    mountains = list(map(int, input().split()))
    peaks = set()
    for i in range(1, len(mountains)-1):
        if mountains[i+1] < mountains[i] > mountains[i-1]:
            peaks.add(i)
    yos = {}
    hehe = 0
    for i in range(len(mountains)):
        yos[i] = hehe
        if i in peaks:
            hehe += 1
    ans = [0, 0]
    for i in range(len(mountains)-1, n-(n-k)-2, -1):
        yos[i] = yos[i] - yos[i - k + 1]
        if i - k + 1 in peaks:
            yos[i] -= 1
        if yos[i] >= ans[-1]:
            ans = [i, yos[i]]
    print(ans[1] + 1, ans[0] - k + 2)
    t -= 1

'''
5
8 6
1 2 4 1 2 4 1 2
5 3
3 2 3 2 1
10 4
4 3 4 3 2 3 2 1 0 1
15 7
3 7 4 8 2 3 4 5 21 2 3 4 2 1 3
7 5
1 2 3 4 5 6 1

'''