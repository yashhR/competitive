def max_sub_array(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        maxis = [nums[0]]
        for i in range(1, len(nums)):
            maxis.append(max(nums[i], maxis[-1] + nums[i]))
        return max(maxis)


print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# This solution beats 82.31% of all python solutions


# 2, 3, -4, 9
