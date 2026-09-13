"""
0. samd direction 2 pointer
- You will have 1 tracker the buy price
- 1 tracking the sell price
- Only will change the buy price when you have so,ething smaller



4. 


"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro = 0
        l = 0
        

        for r, price in enumerate(prices):
            if r == 0 :
                continue
            
            if prices[r] < prices[l]:
                l = r
                # The buy price will move up

            # I will then calu the pro
            profits  = prices[r] - prices[l]
            print(profits)

            max_pro = max(profits, max_pro)

        return max_pro
            