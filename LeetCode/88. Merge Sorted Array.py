def merge(nums1, nums2, m, n):
    first = 0
    second = 0
    while first < m and len(nums2):
        if nums1[first] > nums2[second]:
            nums1.insert(first, nums2.pop(second))
            m += 1
            first += 1
        elif nums1[first] < nums2[second]:
            first += 1
        else:
            nums1.insert(first, nums2.pop(second))
            m += 1
            first += 2
    if len(nums2):
        nums1.extend(nums2)
    return nums1


print(merge([4, 5, 6], [1, 2, 3, 6, 7, 7, 9, 10], 3, 3))