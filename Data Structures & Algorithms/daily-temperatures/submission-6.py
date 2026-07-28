"""
0. When the question gives you that the day has to be warmer only, something that is only inocreaseing or decreasing
- We prob would need to use a stack!!
- Not just a random stack but a monotonically increasing or decreasing stack

1. What do they wnat?
- Return the list of days in front that is less warm. 
- if none return 0 

4. Both space and time will be O(N)
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # It will be a montonoically decreasing stack
        res = [0]*len(temperatures) # prob need to append a tuple!

        for i,temp in enumerate(temperatures):
            
            while stack and temp > stack[-1][0]:
                # so if there are current temp is more, we want to remove all until is monotoically decreasing
                tem, index = stack.pop()
                res[index] = (i - index)

            # Append after
            stack.append((temp, i))
        return res     






