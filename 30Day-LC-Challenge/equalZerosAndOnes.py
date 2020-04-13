
def findMaxLength(nums) -> int:
    counts = {0: -1}
    max_length, count = 0, 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1

        if count in counts.keys():
            max_length = max(max_length, i - counts[count])
        else:
            counts[count] = i
    return max_length
