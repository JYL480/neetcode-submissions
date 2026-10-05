"""
0. stupid monkey
anywasy if you they ask you to find a rate or soemthig right! You will know that this likelly will be binary search aldy ayh

1. What do they want?
- return an integer for this when the total consumtiption hour is less than h

4. We will just skip to see if we can do this yah

5. Complexity?
O(N log (R)) likely will be this yah cause it is binary saerhc  R is the search space of eatiing 
spacee O(1)

"""

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 # Lowest will be 1  
        r = max(piles)
        min_rate = float('inf')

        while l <= r:
            mid = (l) + (r - l)//2 # LOL
            total_hours = 0
            for bana in piles:
                total_hours += math.ceil(bana/mid)
            print(mid,total_hours)

            if total_hours > h:
                # Can be smoller so we will move down 
                l= mid +1

            elif total_hours <= h: # then we are good 
                min_rate = min(min_rate, mid)
                r = mid - 1

        return min_rate


            









        