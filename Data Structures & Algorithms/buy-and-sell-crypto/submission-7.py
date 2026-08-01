class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       # For each possible buy day, what's the best sell day
        left = 0
        dif_main = [0]
        while left < len(prices):
            window = prices[left:]
            i = 0
            dif = [0]
            while i < len(window):
                if window[i] - window[0] > 0:
                    dif.append(window[i] - window[0])
                i += 1
            dif_main.append(max(dif))
            left += 1
    
        return max(dif_main)
            

            






