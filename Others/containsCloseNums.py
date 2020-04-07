def answer(nums, k):
    bitch = {}
    for i in range(len(nums)):
        if nums[i] in bitch:
            if abs(i-bitch[nums[i]]) <= k:
                return True
            else:
                bitch[nums[i]] = i
        else:
            bitch[nums[i]] = i
    return False


print(answer([0, 1, 2, 3, 5], 2))
