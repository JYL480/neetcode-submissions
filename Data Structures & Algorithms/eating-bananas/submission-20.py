"""
0. Lets try koko eating a banan yay!!
- What is this? The first intuition is that you iwl
- This is immediately a binary search for this yah 
- Well because then want you to find the speed, and then you know what is the bound
- 1 is the slowest and max is the piles loh, so this is your boundary


1. What does the q wawnt??
- Want to return the intergr
- whiwh the min speed such that it can eat all within h hours 
- 

4.  pattern
- Binary search 
- Also what is the moving condition
- If more than target, can move up 
Less than target, right move down

# I will be using math ceiling? for this? yes!!! Okay movingn on!


"""

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) # This is O(n) yah
        min_r = float('inf')
        while l<=r:
            mid_r = (l + r)//2 #so this is the thing we want yah
            print(l, r, mid_r)
            total_time = 0 
            for ban in piles:
                total_time += math.ceil(ban/mid_r)
            print("time",total_time)
                
            if total_time > h: # meaing too slwo 
                l = mid_r + 1
            elif total_time <= h: # have time to spare, we want the min right 
                r = mid_r - 1
                min_r = min(mid_r, min_r)
                print(min_r)
            

        
        return min_r









        