str = list(map(int, input().split()))
odd = []
even = []
for i in str:
    if str.index(i) % 2 == 0:
        odd.append(i)
    else:
        even.append(i)

odd.sort()
even.sort(reverse=True)

for i in range(len(even)):
    print(odd[i])
    print(even[i])