class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_profit = 0
        best_profit = 0

        left = 0
        right = 1

        while right < len(prices):
            current_profit = prices[right] - prices[left]
            if current_profit <= 0:
                left = right

            else:
                best_profit = max(best_profit, current_profit)
            right += 1
        return best_profit