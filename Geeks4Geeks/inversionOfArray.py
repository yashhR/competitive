'''
Given an array of positive integers. The task is to find inversion count of array.

Inversion Count : For an array, inversion count indicates how far (or close) the array is from being sorted.
If array is already sorted then inversion count is 0.
If array is sorted in reverse order that inversion count is the maximum.
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N, the size of array. The second line of each test case contains N elements.

Output:
Print the inversion count of array.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107
1 ≤ C ≤ 1018

Example:
Input:
1
5
2 4 1 3 5

Output:
3

Explanation:
Testcase 1: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
'''


# t = int(input())
# while t:
#     n = int(input())
#     arr = list(map(int, input().split()))
#     c = 0
#     for i in range(n):
#         for j in range(i+1, n):
#             if arr[i] > arr[j]:
#                 c += 1
#     print(c)
#     t -= 1


t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    stack = []
    c = 0
    for num in arr:
        if len(stack) == 0:
            stack.append(num)
            continue
        if num < stack[-1]:
            i = len(stack) - 1
            while i >= 0 and num < stack[i]:
                i -= 1
                c += 1
            if i == -1:
                stack.insert(0, num)
            else:
                stack.insert(i+1, num)
        else:
            stack.append(num)
    #     print(f"stack: {stack}")
    # print(stack)
    print(c)
    t -= 1