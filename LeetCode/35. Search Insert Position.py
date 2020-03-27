class Solution:
    def searchInsert(self, nums, target: int) -> int:
        prevMid = 0
        def bS(a, start, end, val):
            temp = None
            if start <= end:
                mid = start + (end-start)//2
                Solution.prevMid = mid
                if a[mid] == val:
                    return mid
                elif a[mid] > val:
                    temp = 0
                    return bS(a, start, mid-1, val)
                else:
                    temp = 1
                    return bS(a, mid+1, end, val)
            else:
                if nums[Solution.prevMid] > val:
                    return Solution.prevMid
                else:
                    return Solution.prevMid + 1
        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        start = 0
        end = len(nums) - 1
        return bS(nums, start, end, target)