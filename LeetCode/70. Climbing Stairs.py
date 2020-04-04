'''
70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

'''
I'm thinking DP.
The base case is that you can get onto the first step in only 1 step and maybe we can build on the fact that
to each any step (other than the first step), there's two ways to do it, come for a step that is two steps below it
and come from a step that is one step below it.

We calculate the no. of steps for a point and build on that. Bottom UP approach

'''


def climb_stairs(n):
    dp = {0: 1, 1: 1}
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


