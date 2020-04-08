'''
Input:

First line will contain integer T, number of test cases.

Second line will contain integers **  ** (their meanings are mentioned in problem statement)

Output:

Print the integral result, minimum time (in minutes) to reach city B in a new line.

Constraints:





SAMPLE INPUT
1
5 5 8 100 90 320
SAMPLE OUTPUT
197
Explanation
Roy reaches station A in 5 minutes, First train departs in 5 minutes and second train departs in 8 minutes,
he will be able to catch both of them. But he has to make an optimal choice, which train reaches city B in minimum time.
 For first train  minutes. Total time for first train,  minutes

For second train  minutes. Least integer greater than . Total time for second train  minutes.
So optimal choice is to take first train, and hence the minimum time is  minutes.
'''

t = int(input())
for _ in range(t):
    t0, t1, t2, v1, v2, d = map(int, input().split())
    if t1 < t0 and t2 < t0:
        print(-1)
    else:
        train1time = d / v1 * 60
        train2time = d / v2 * 60
        if t0 <= t1 and t0 <= t2:
            print(min(t1 + train1time, t2 + train2time))
        elif t1 >= t0 > t2:
            print(round(t1 + train1time))
        elif t1 < t0 <= t2:
            print(round(t2 + train2time))
