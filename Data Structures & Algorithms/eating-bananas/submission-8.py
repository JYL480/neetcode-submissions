"""
0. we need tofind the speed. 
- That matches the condition
- How do we decide on the speed?
- Then what?
- 1 to max(piles)
- WE can think of this as the ordered list we are workin with
- Binary search to find the right one for us


4. Pattern
- So it will be a binary search
- You will get the min() of the speed lol
- We also need to know how to caculate the timing which is the use math.ceil()
- 

5. complexity 

There will be logn somehwere?
might be a nlogn idk 




"""

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l , r = 1, max(piles)
        min_eat = float('inf')

        while l <= r:
            
            cur_speed = (l + r) // 2

            total_hours = 0
            
            for num_bana in piles:
                total_hours += math.ceil(num_bana/cur_speed)

            if total_hours > h: # Meaning we are taking too long, need to be faster thus left will move up 
                l = cur_speed + 1
            elif total_hours <= h: # meaning okay, can afford to be slower
                r = cur_speed - 1
                min_eat = min(cur_speed, min_eat)

        
        return min_eat
            












        