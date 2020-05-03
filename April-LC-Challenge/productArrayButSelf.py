def product_except_self(nums):
    lefts = [1]
    rights = [1]
    result = []
    for i in range(1, len(nums)):
        lefts.append(lefts[-1]*nums[i-1])
    for i in range(len(nums)-2, -1, -1):
        rights.insert(0, rights[0]*nums[i+1])
    for i in range(len(nums)):
        result.append(lefts[i]*rights[i])
    # print(lefts)
    # print(rights)
    return result


print(product_except_self([1, 2, 3, 4]))
# This solution works but not in constant space


# Approach 2

def product_but_self_2(nums):
    result = [1]
    for i in range(1, len(nums)):
        result.append(result[-1]*nums[i-1])
    rights = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] = result[i]*rights
        rights = rights*nums[i]
    return result


print(product_but_self_2([1, 2, 3, 4]))