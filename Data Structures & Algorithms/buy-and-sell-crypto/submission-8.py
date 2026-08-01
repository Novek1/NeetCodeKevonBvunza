class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       # For each possible buy day, what's the best sell day
        left = 0
        right = 1
        maxP = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(maxP , profit )
            else :
                left = right
            right += 1

        return maxP            

            






