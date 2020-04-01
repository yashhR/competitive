'''
You are developing a smartphone app.
You have a list of potential customers for your app.
Each customer has a budget and will buy the app at your declared price
if and only if the price is less than or equal to the customer's budget.


You want to fix a price so that the revenue you earn from the app is maximized. Find this maximum possible revenue.
For instance, suppose you have 4 potential customers and their budgets are 30, 20, 53 and 14.
In this case, the maximum revenue you can get is 60.


Input format
Line 1 : N, the total number of potential customers.

Lines 2 to N+1: Each line has the budget of a potential customer.


Output format
The output consists of a single integer, the maximum possible revenue you can earn from selling your app.


Sample Input 1
4
30
20
53
14

Sample Output 1
60

Sample Input 2
5
40
3
65
33
21

Sample Output 2
99

Test data
Each customers' budget is between 1 and 108, inclusive.


Subtask 1 (30 marks) : 1 ≤ N ≤ 5000.

Subtask 2 (70 marks) : 1 ≤ N ≤ 5×10**5.


Live evaluation data
There are 15 test inputs on the server during the exam. The grouping into subtasks is as follows.

• Subtask 1: Test inputs 0,…,5

• Subtask 2: Test inputs 6,…,14



Note
The answer might not fit in a variable of type int.
We recommend that you use variables of type long long to read the input and compute the answer.
If you use printf and scanf, you can use %lld for long long.
'''


# N = int(input())
# budgets = []
# for i in range(N):
#     budgets.append(int(input()))
#
# budgets.sort()
# maxi = 0
# i = 0
# while i < len(budgets):
#     budgets[i] = budgets[i] * (N-i)
#     if budgets[i] > maxi:
#         maxi = budgets[i]
#     count = 1
#     if i != len(budgets) - 1:
#         while budgets[i+1] == budgets[i]:
#             count += 1
#         i += count
#     else:
#         i += 1
# print(maxi)

# This passed all the test cases (100/100)


# [30, 20, 53, 14] ~ [14, 20, 30, 53] = [14*4, 20*3, 30*2, 53*1]
# [30, 30, 30, 30] ~ [30, 30, 30, 30] = [120]


# N = int(input())
#
# budgets = {}
#
# while N > 0:
#     n = int(input())
#     if n in budgets:
#         budgets[n] += 1
#     else:
#         budgets[n] = 0
#         if len(budgets) > 0:
#             for item in budgets:
#                 if item >= n:
#                     budgets[n] += 1
#                 else:
#                     budgets[item] += 1
#     N -= 1
#
# maxi = 0
# for item in budgets:
#     if item*budgets[item] > maxi:
#         maxi = item*budgets[item]
#
# print(maxi)
# This passed all tcs in subtask 1 and one tc in subtask 2 (30/100)
