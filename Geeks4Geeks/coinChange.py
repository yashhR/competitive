'''
Given a value N, find the number of ways to make change for N cents,
if we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins.
The order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4.
For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}.
So the output should be 5.

Input:
The first line contains an integer 'T' denoting the total number of test cases.
In each test cases, the first line contains an integer 'M' denoting the size of array.
The second line contains M space-separated integers A1, A2, ..., AN denoting the elements of the array.
The third line contains an integer 'N' denoting the cents.

Output:
Print number of possible ways to make change for N cents.

Constraints:
1 ≤ T ≤ 50
1 ≤ N ≤ 300
1 ≤ A[i] ≤ 300

Example:
Input:
2
3
1 2 3
4
4
2 5 3 6
10

Output:
4
5

Explanation:
Testcase 1: The possiblities are as such: {1, 1, 1, 1}, {1, 1, 2}, {1, 3}, {2, 2}.
'''

t = int(input())


def ans():
    n = int(input())
    coins = list(map(int, input().split()))
    cents = int(input())
    table = [[0 for x in range(cents+1)] for y in range(len(coins)+1)]
    table[0][0] = 1
    for i in range(len(coins)+1):
        table[i][0] = 1
    for i in range(len(coins)+1):
        print(table[i])
    for i in range(1, len(coins)+1):
        for j in range(1, cents+1):
            if j >= coins[i-1]:
                table[i][j] = table[i][j-coins[i-1]] + table[i-1][j]
            else:
                table[i][j] = table[i-1][j]
    for i in range(len(coins)+1):
        print(table[i])
    return table[len(coins)][cents]


for _ in range(t):
    print(ans())
