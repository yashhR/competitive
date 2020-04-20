'''
Given an array, find the next greater element G[i] for every element A[i] in the array.
The Next greater Element for an element A[i] is the first greater element on the right side of A[i] in array.
More formally,

G[i] for an element A[i] = an element A[j] such that
    j is minimum possible AND
    j > i AND
    A[j] > A[i]
Elements for which no greater element exist, consider next greater element as -1.

Example:

Input : A : [4, 5, 2, 10]
Output : [5, 10, 10, -1]

Example 2:

Input : A : [3, 2, 1]
Output : [-1, -1, -1]
'''


# def next_greater(A):
#     maxi = max(A)
#     for i in range(len(A)-1):
#         if A[i] == maxi:
#             A[i] = -1
#             continue
#         found = False
#         for j in range(i+1, len(A)):
#             if A[j] > A[i]:
#                 found = True
#                 A[i] = A[j]
#                 break
#         if not found:
#             A[i] = -1
#     A[-1] = -1
#     return A
#
#
# print(next_greater([4, 5, 2, 10]))


'''
The above is an O(n^2) solution.
The idea is that for every element in the array, we go through the array to the right of it and if we find a value
greater than our element, then we substitute the element with our value, break the checking and go to the next element.
If not found, that means our element is the greatest in the array and we put it as -1.

For the last element, we dont have anything to look right to, hence we put it as -1. And finally we return the array.
'''


def getGth(A, st):
    print(A, st)
    while len(st) > 0:
        if st[-1] > A:
            return st[-1]

        st.pop()
    return -1


def nextGreater(A):
    st = []
    gts = []
    for i in range(len(A) - 1, -1, -1):
        gts.append(getGth(A[i], st))
        print(gts, st)
        st.append(A[i])

    return gts[::-1]


print(nextGreater([4, 5, 6, 10]))