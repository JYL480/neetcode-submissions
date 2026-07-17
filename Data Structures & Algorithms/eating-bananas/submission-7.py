"""

0. Let me do this again hoho
lets recap the  concetps??
- YOu only can binary search with what?
- You acn oly binary search when you have something sorted!!
- So porb most likely will be the nyumbers
- Then you have to find out what the hell is sorted hor 


- So in this case, you are ask to find the speed of eating
- That will satisfy the condition
- What is the sorted here?
- the low to high boundary 
- So just search in between here loh


1. What do they want?
- find the rate such that the total hour spent will beless than h?

skip

4. How to do 
using binary search

1st - we needd to find the boundaris
2nd decide how to claculate the time taken
3rd then to binary searh 

"""
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)
        res= float('inf')
        
        # How to caculate time taken? Prob will be ceiling

        while min_speed <= max_speed:
            mid = (min_speed + max_speed) //2
            time_taken = 0
            for num in piles:
                time_taken += math.ceil(num/mid)
            print("time tak: midn",time_taken,mid)

            if time_taken > h: # Here will be valid, meaning it will be lesse
                # We can afford to be faster
                min_speed = mid + 1

            elif time_taken <= h:
                max_speed = mid - 1
                print(mid)
                res = min(mid, res)
            

        return res





        