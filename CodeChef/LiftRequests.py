t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    present = 0
    answer = 0
    while q:
        f, d = map(int, input().split())
        answer += abs(present-f) + abs(f-d)
        present = d
        q -=1
    print(answer)