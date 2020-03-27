def threeSumClosest(nums, target):
    nums.sort()
    print(nums)
    for i in range(len(nums) - 2):
        if i == 0 or i > 0 and nums[i] != nums[i-1]:
            left = i + 1
            right = len(nums) - 1
            minimum = 100000000000
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                print(f"sum for {i}, {left} and {right} is {s}")
                if s == target:
                    return target
                elif s > target:
                    if abs(target - s) < minimum:
                        minimum = abs(target - s)
                        newsum = s
                    right -= 1
                else:
                    if abs(target - s) < minimum:
                        minimum = abs(target - s)
                        newsum = s
                    left += 1
                print("minimum is:", minimum)
    return newsum


print(threeSumClosest([1,1,1,0], -100))