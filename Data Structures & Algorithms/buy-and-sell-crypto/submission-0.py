class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Edge Case
        if len(prices) <= 1:
            return 0
        
        left, right = 0, 1
        maxProfit = 0

        while right < len(prices):
            print(f"left is {left}-{prices[left]}, right is {right}-{prices[right]}, maxProfit is {maxProfit}")
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                print(f"profit is {profit}")
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1

        return maxProfit
