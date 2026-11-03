class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_profit = 0
        max_profit = 0

        left = 0
        right = 1

        while(right<len(prices)):
            current_profit = prices[right] - prices[left] 
            if current_profit < 0:
                print("Moved left")
                left = right
            else:
                right += 1
            max_profit = max(current_profit, max_profit)
            print("New max is:", max_profit)
            
        return max_profit
        