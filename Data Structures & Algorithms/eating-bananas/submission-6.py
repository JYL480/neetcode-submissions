"""

1. They want you to return the min each rate, such that we fufil h hours
- return an integer value
- k hass to be efficient
- Have to find a minium value of K?


2. Edge cases?
- value of bananaan 1?


3. naive?
- Nested for loop loh how and count how many count it takes to emoty each index

4. Pattern

FIrst we have decide how to long does it take to each index to finish the banan

- Which is ceil(x/k)

- the sum of all (ceil(x/k)) <= h 

- What is the upper bound for k?
- max will be the laragest

- We have to determine what is our search sapce, and what is the upper and lower bound of ourr search space
- 1 is the lowest we can go 
- max(pile) is the highest i
- We do a binary seardch onn this search sapce and see to find the min

if count <= h, meaning we can afford to go slower, move r to mid - 1
if count > h, meaning we only have to be faster to be meet the hours, thus the left have to mid + 1  

"""
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        highest = max(piles)
        lowest = 1
        s_space = []

        
        l , r = 1, highest 
        final_speed = 0


        while l <= r:

            speed = (l + r) //2

            hours = 0
            for ban in piles:
                hours += math.ceil(ban/speed)

            if hours <= h: # Means we acn afford to be slower
                r = speed - 1
                final_speed = speed
            elif hours > h: # Means the speed now not valid and we need to be faster 
                l = speed + 1
        return final_speed









        