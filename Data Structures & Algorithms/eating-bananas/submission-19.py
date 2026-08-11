"""
0. Intuition 
- If you talk about speed, finding the right speed, then it will be sorted right
- If something is sorted, what is the first thing, we should thinkg of binary search
- Rmb how to do this shit right
- You need to half the searrch space everytime. 
- With this, You you want to find n n

- OKay I think I will write a cheat sheet for these bah. Good to hor. Should be seconod nature to me.....



1. What does thequestion wna?
- Want to return the int which is th erate of eating the banan
- It has to be min. So there needs to be a serarch space of how to get the banan rate
- 

4. PAttern?
- Okayy I will figure what is the low and max it can go. 
- Also have a min_rate to track which one is the lowest
- How do we calculate
- Usisng floor bah to then cacuale that shit IDK


"""


import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowest = 1
        highest = max(piles)

        # The above will be our searrch space
        l,r = 1, highest

        min_rate = highest
                    # We can only move l if we got spare time else move right down
        while l <= r:
                mid = (l + r) //2
                total_hours = 0

                for i, bana in enumerate(piles):
                    total_hours += math.ceil(bana/mid)             

                if total_hours <= h:
                    r = mid - 1
                    min_rate = min(mid, min_rate)
                elif total_hours >h:
                    l = mid + 1

        return min_rate












        