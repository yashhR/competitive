'''
Chef made N pieces of cakes, numbered them 1 through N and arranged them in a row in this order.
There are K possible types of flavours (numbered 1 through K); for each valid i, the i-th piece of cake has a flavour Ai.

Chef wants to select a contiguous sub-segment of the pieces of cake such that-
there is at least one flavour which does not occur in that subsegment.
Find the maximum possible length of such a subsegment of cakes.

Input:

The first line of the input contains a single integer T denoting the number of test cases.
The description of T test cases follows.
The first line of each test case contains two integers N and K.
The second line contains N space-separated integers A1,A2,…,AN.


Output:  For each test case, print a single line containing one integer ― the maximum length of a valid subsegment.

Example Input:
2
6 2
1 1 1 2 2 1
5 3
1 1 2 2 1
Example Output:
3
5
'''
t = int(input())


def longest_sub():
    n, k = map(int, input().split())
    flavours = list(map(int, input().split()))
    for i in range(n-1):
        for j in range(n-1, 0, -1):
            c = len(set(flavours[i:j+1]))
            if c < k:
                return len(flavours[i:j+1])


for i in range(t):
    print(longest_sub())
