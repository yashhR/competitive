def threeSum(nums):
    nums.sort()
    print(nums)
    lookup = {}
    triplets = []
    tripsHash = {}
    for i in range(len(nums)):
        lookup[nums[i]] = i
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            pT = 0 - nums[i] - nums[j]
            if pT in lookup and lookup[pT] != i and lookup[pT] != j:
                pos = [nums[i], nums[j], pT]
                pos.sort()
                if f"{pos}" not in tripsHash:
                    triplets.append(pos)
                    tripsHash[f"{pos}"] = True
    return triplets


print(threeSum([-1, 0, 1, 2, -1, 4]))

# from itertools import combinations
#
# def ans(nums):
#     combs = list(combinations(nums, 3))
#     maybe = []
#     combs = map(lambda x: list(x), combs)
#     combs = list(combs)
#     for i in range(len(combs)):
#         combs[i].sort()
#         if sum(combs[i]) == 0:
#             if combs[i] not in maybe:
#                 maybe.append(list(combs[i]))
#     return maybe


# print(ans([-1, 0, 1, 2, -1, 4]))


'''
If a list has lists that have the same elements but in different order, consider them as the same element and
make the list unique.
i.e.,
Make a set of given lists
'''

