# def permute(nums):
#     retList = [nums]
#     for i in range(len(nums)):
#         j = 0
#         while j < len(nums):
#             haha = []
#             for k in range(len(nums)):
#                 haha.append(nums[k])
#             haha[i], haha[j] = haha[j], haha[i]
#             print(haha)
#             print(retList)
#             if haha not in retList:
#                 retList.append(haha)
#             print(retList)
#             j += 1
#     return retList
#
#
# print(permute([1, 2, 3]))


def permutate(lst):
    if len(lst) == 0:
        yield []
    elif len(lst) == 1:
        yield lst
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in permutate(xs):
                yield [x]+p
        return l
answers = []
for p in permutate([1, 2, 3]):
    answers.append(p)
print(answers)