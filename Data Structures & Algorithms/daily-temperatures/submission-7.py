"""
0. Intuition, this qurestion asks for soehting that is lawyas increasing..... 
- Immediaely or something that is 
- Next greatest is larger or smaller etc.. 
- And you are in a stack yah 



3. If you use this monotolically decreasing stack or decreasing, it will 
- O(N) for time
- O(N) for space as well

- Because you will only pop the thing from the stack only 1, so will not have a nested yah


4. Pattern
- You will have monotonically decreasing stack
- There will be a while loop inside yah, which will see whether the thingy is accurate 



"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        res = [0] * len(temperatures) # This will be it loh becauee we will be using indexinng yah 

        # stack should store a tuple yah, with the temp andindex

        for i, temp in enumerate(temperatures):
            
            while stack and temp > stack[-1][0]:
                # Because the current temp is is larger, will pop out
                p_temp, p_i = stack.pop()

                len_res = i - p_i
                res[p_i] = len_res



            stack.append((temp,i))

        return res







