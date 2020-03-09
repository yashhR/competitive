'''
Given an array, find the number which has the same sum of numbers on it's either side

Solution:
On it's either side, meaning - we got to find the position -
sum of all the numbers from before the position to the beginning of the array is equal to
sum of all the numbers after the position to the end of the array.

Let us see the usual approach first:
the function bf_get_equi(arr) is the brute-force approach.

For each index, we are getting the sum of elements to its left and elements to its right
This makes it O(n(n + n)) => O(2n^2) => O(n^2)
'''


def bf_get_equi(arr):
    n = len(arr)
    for i in range(n):
        sum1 = 0
        sum2 = 0
        #if sum(arr[:i]) == sum(arr[i+1:]):
        for j in range(0, i):
            sum1 += arr[j]
        for j in range(i+1, n):
            sum2 += arr[j]
        if sum1 == sum2:
            return arr[i]


print(bf_get_equi([1, 2, 3, 4, 6]))


'''
What we can do it instead, is get some more space and
to avoid repeated addition, we instead store the addition of lefts and rights of each index
what this means is:

suppose for an index, you have calculated the lefts of that index
now, for the next index, you don't have to start again from the starting to that index,
what you can do is:  **store the lefts of the previous index and just add the previous index value to it** [main]

What we are basically doing is avoiding repetitive work and that is by storing the repetitive work
So,

what we know for sure is, the sum of elements to the left of the first index is 0
and sum of elements to the right of the last index is 0
lets store them, lefts = {0: 0}
                 rights = {n-1: 0}
now, from [main] point,
            here, we start looping from 1st index to last index, because there's no value of index i-1 for i = 0 and we have stored
            lefts[0] anyway
                lefts[1] becomes lefts[0] + value at index 0
                lefts[2] becomes lefts[1] + value at index 1
                lefts[3] becomes lefts[2] + value at index 2
                lefts[i] becomes lefts[i-1] + value at index i-1
the same thing for rights
            here, we come from the back (index n-2) as n-1 is already stored, 
            and go until -1 so that we include 0 index as well
            if array size is 6, we know rights[5] is 0
            rights[4] = rights[5] + value at index 5
            rights[3] = rights[4] + value at index 4
            rights[2] = rights[3] + value at index 3
            rights[i] = rights[i+1] + value at index i+1
'''


def get_equi(arr):
    n = len(arr)
    lefts = {0: 0}
    rights = {n-1: 0}
    for i in range(1, n):
        lefts[i] = arr[i-1] + lefts[i-1]
    for i in range(n-2, -1, -1):
        rights[i] = arr[i+1] + rights[i+1]
    for i in range(n):
        if lefts[i] == rights[i]:
            return arr[i]


print(get_equi([1, 2, 3, 4, 6]))


