t = int(input())
while t:
    n = int(input())
    okay = list(map(int, input().split()))
    occured = set()
    hehe = {}
    i = 0
    done = False
    while i < n:
        if okay[i] not in hehe:
            temp = okay[i]
            count = 0
            while i < n and okay[i] == temp:
                count += 1
                i += 1
            hehe[temp] = count
            if count in occured:
                done = True
                print("NO")
                break
            else:
                occured.add(count)
        else:
            done = True
            print("NO")
            break
    if not done:
        print("YES")
    t -= 1