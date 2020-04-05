t = int(input())
for _ in range(t):
    x = int(input())
    n = int(input())
    password = list(map(int, input().strip().split()))
    m = int(input())
    bobs = list(map(int, input().split()))
    i = 0
    count = 0
    while i <= m - n:
        possible_answer = bobs[i:i+n]
        bitch = abs(password[0] - possible_answer[0])
        answer = False
        if bitch <= x:
            for j in range(n):
                if abs(password[j]-possible_answer[j]) == bitch:
                    answer = True
                else:
                    answer = False
                    break
        if answer:
            count += 1
        i += 1
    print(count)
