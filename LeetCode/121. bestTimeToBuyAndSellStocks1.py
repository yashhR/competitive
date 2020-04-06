class Solution:
    def maxProfit(prices) -> int:
        if len(prices) == 1 or len(prices) == 0:
            return 0
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            min_price = min(prices[i], min_price)
            potential_profit = prices[i] - min_price
            max_profit = max(max_profit, potential_profit)
        return max_profit
