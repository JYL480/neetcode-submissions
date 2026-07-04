"""
0. What wis this ????
have a monotonic stack for this!!
And you will be doing this 

- a monotonic stack 
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        for i, temp in enumerate(temperatures):
            
    
            while stack and temp > stack[-1][0]:
                index = stack[-1][1]
                dist = i - index
                res[index] = dist
                stack.pop()
                

            stack.append((temp, i))
        return res





            
        
    










