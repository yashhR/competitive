bros = list(map(str, input().split()))
nums = []
alphas = []

for i in range(len(bros)):
    if i%2 == 0:
        nums.append(int(bros[i]))
    else:
        alphas.append(bros[i])

nums.sort()
alphas.sort()

for i in range(len(nums)):
    print(nums[i], end=" ")
    print(alphas[i], end=" ")