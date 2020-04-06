n, m = map(int, input().split())
votes = list(map(int, input().split()))
total = sum(votes)
satisfied = [x for x in votes if x >= total * (1/(4*m))]
if len(satisfied) >= m:
    print("Yes")
else:
    print("No")
