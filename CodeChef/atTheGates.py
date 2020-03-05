'''
There is a table in front of you, with N coins placed in a row and numbered 1 through N from left to right.
For each coin, you know whether it is initially showing heads or tails. You have to perform exactly K operations.
In one operation, you should remove the rightmost coin present on the table,
and if this coin was showing heads right before it was removed, then you should also flip all the remaining coins.
(If a coin was showing heads, then after it is flipped, it is showing tails, and vice versa.)

The code needed to enter the temple is the number of coins which, after these K operations are performed,
have not been removed and are showing heads. Can you find this number? The fate of Persia lies in your hands…

Input:

The first line of the input contains a single integer T denoting the number of test cases.
The description of T test cases follows.
The first line of each test case contains two space-separated integers N and K.
The second line contains N space-separated characters.
For each valid i, the i-th of these characters is 'H' if the i-th coin is initially showing heads or 'T' if it is showing tails.


Output:
For each test case, print a single line containing one integer ― the number of coins that are showing heads after K operations.
'''


t = int(input())


def how_many():
    n, m = map(int, input().split())
    coins = list(input().split())

    def flip():
        for i in range(len(coins)):
            if coins[i] == "H":
                coins[i] = "T"
            else:
                coins[i] = "H"
    for i in range(m):
        if coins[-1] == "H":
            flip()
        coins.pop()
    count = 0
    for i in range(len(coins)):
        if coins[i] == "H":
            count += 1
    return count


for i in range(t):
    print(how_many())
