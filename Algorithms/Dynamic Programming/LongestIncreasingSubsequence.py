'''
Problem: Given a array of integers, return the length of the longest non-decreasing subsequence

We will be using Dynamic Programming to solve this problem.
If you prefer a video explanation for this problem - check out Back to Back SWE.

Subsequence: Any subset of the given array that maintains the order of elements as they occur in the og array.

Idea: For every element, we will store the length of the longest subsequence from the beginning of the array
      till that element i.e.,

      These are the subproblems, and when we reach the last element, we would have stored the lengths of all
      possible non decreasing subsequences and we can get the max of them.

      We maintain an extra array which, at each index, stores the max subseq length from the beg to that index in oga.

      We initialize the array with 1 because the element itself is a subseq and it is non decreasing because there's
      nothing else to even compare to.

      Now, we start from the 2nd element (index 1) and go through all indices before it.
      At this point, what we are esentially doing is that we are asking if this current element we are at can
      contribute to any of the subsequences that have occurred before.

      As we need to do this for all subseqs that may have occured before - we go through all elements before this
      element and if we can contribute (that curr element is greater than or equal to the before element), we now check
      if this addition to that subseq results in a longer subseq than the curr longest within the bounds, if yes -
      we add 1 to the stored length of subseq of the before element, else - we maintain the curr longest as it is.
'''


def solve(a):
    n = len(a)
    dp = [1 for x in range(n)]
    for j in range(1, n):
        for i in range(j):
            if a[j] >= a[i]:   
                dp[j] = max(dp[j], dp[i] + 1)
    return max(dp)


print(solve([-1, 3, 4, 5, 2, 2, 2, 2]))
