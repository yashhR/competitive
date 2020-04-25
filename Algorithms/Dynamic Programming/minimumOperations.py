'''
You are given a number N. You have to find the number of operations required to reach N from 0.
You have 2 operations available:
1. Double the number
2. Add one to the number

Input:
    The first line of input contains an integer T denoting the number of test cases.
    Then T test cases follow. Each test case contains an integer N.

Output:
    For each test case, in a new line, print the minimum number of operations required to reach N from 0.

Constraints:
    1<=T<=100
    1<=N<=104

Example:
Input:
2
8
7
Input:
4
5

Explanation:
Testcase1:
Input  : N = 8
Output : 4
0 + 1 = 1, 1 + 1 = 2, 2 * 2 = 4, 4 * 2 = 8
Testcase2:
Input  : N = 7
Output : 5
0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 3 * 2 = 6, 6 + 1 = 7


100
+1
+1
+1
*2
*2
*2
+1
*2
*2
'''


t = int(input())
while t:
    n = int(input())
    if n % 2 == 0:
        count = 0
        while n > 0:
            while n % 2 == 0:
                count += 1
                n = n//2
            n -= 1
            count += 1
    else:
        count = 1
        n -= 1
        while n > 0:
            while n % 2 == 0:
                count += 1
                n = n//2
            n -= 1
            count += 1
    print(count)
    t -= 1