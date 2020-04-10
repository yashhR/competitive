n = int(input())
array = list(map(int, input().split()))
count = 0
for i in range(len(array)):
    for j in range(i, len(array)):
        print(array[i:j+1])
        if sum(array[i:j+1]) % 2 == 0:
            count += 1
print(count)
