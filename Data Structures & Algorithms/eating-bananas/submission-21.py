"""
0. Now lets see what this is?
- This is koko eating banana thingy yah
- Note that we hve to find what is correct rate to eat all the bananas?
- This will be what?
- Becauser we are finding a speed and it is ordered, and we are searching likely will be bbinary search 

1. What does it want?
- They want to return a the int of which the can eat all the bananan within the hours given 
- You will need to floor something yah 


4. pattern 
- low = 1
high will be the max banana in the list 

5. Complexity 
Binary search complexity 
Time comeplxti will be Nlog(MaxOfN)  which is okay 


"""

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_rate = 1
        max_rate = max(piles)
        best_rate = float('inf')

        # Woah how to do binary search
        while min_rate <= max_rate:
            mid_rate = (min_rate + max_rate) //2

            total_eating_time = 0 

            for bana in piles:
                total_eating_time += math.ceil(bana/mid_rate)

            if total_eating_time > h:
                # We need to be faster
                min_rate = mid_rate + 1
            
            elif total_eating_time <= h:
                max_rate = mid_rate - 1
                best_rate = min(best_rate, mid_rate)

            print(total_eating_time, mid_rate, best_rate)
        return best_rate
            

            









        