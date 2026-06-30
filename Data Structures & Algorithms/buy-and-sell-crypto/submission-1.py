"""
0. THis is new concept yah, we are doing sliding window yay!!!

1. They wan tyou to return an integer
- max profit!!1

2. edge?

3. Naive?
- you can do a nested again loh

4. Sliding window?


"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        buy = float("inf")
        for i, sell in enumerate(prices):
            if sell <= buy: 
                buy = sell
            
            prof = sell - buy
            print(sell, buy)
            maxProf = max(prof, maxProf)
        return maxProf

        