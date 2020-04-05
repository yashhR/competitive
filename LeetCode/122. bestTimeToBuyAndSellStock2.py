'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''


# def max_profit_with_single_transaction(prices):
#     minimum_price = prices[0]
#     maximum_profit = 0
#     for i in range(1, len(prices)):
#         minimum_price = min(prices[i], minimum_price)
#         potential_profit = prices[i] - minimum_price
#         maximum_profit = max(maximum_profit, potential_profit)
#     return maximum_profit
#
#
# print(max_profit([7, 6, 2, 3, 1]))


def max_profit(prices):
    if len(prices) == 0 or len(prices) == 1:
        return 0
    profit = 0
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            profit += prices[i+1] - prices[i]
    return profit


print(max_profit([7, 1, 5, 3, 6, 4]))