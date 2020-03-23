def maxArea(height) -> int:
    maxArr = 0
    i = 0
    j = len(height) - 1
    while i < j:
        mini = (min(height[i], height[j]))
        maxArr = max(maxArr, mini * (j - i))
        if height[i] < height[j]:
            i += 1;
        else:
            j -= 1
    return maxArr

print(maxArea([1,2,100,1,1,1,1,1,2]))