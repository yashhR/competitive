def solution(nums):
    i = 0
    ret_list = []
    while i < len(nums):
        start = nums[i]
        while i < len(nums)-1 and nums[i+1] == nums[i] + 1:
            i += 1
        end = nums[i]
        if start != end:
            ret_list.append(f"{start}->{end}")
        else:
            ret_list.append(f"{start}")
        i += 1
    return ret_list


print(solution([-1, 0, 1, 2, 6, 7, 9]))
