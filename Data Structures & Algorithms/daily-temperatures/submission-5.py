"""

0. We want to use mnonnotically decreqaseing stack?
- WHy decreasing?
- We want to calculage how many days has been that has slower temp that that day....
- So decreaseting the best bet 



4. Pattern
- Will use a stack for this 

"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                # If the today temp is way higher and not lesser, then will have to popo until false loh
                # How to cal the day?
                length = i - stack[-1][1]
                res[stack[-1][1]] = length
                stack.pop()

            stack.append((temp, i))

            print(stack)
        return res
    










