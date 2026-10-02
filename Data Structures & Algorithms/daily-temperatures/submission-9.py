"""
0. What is the intuition here?
- They want a always inceraseing, i Would think they want a monotonically increasing stack bah
- note that we will the removeingn thingy first tehn append, most of the question will be like this yah 
- remove first then you will add!!

- Because we want to count how many days right, this will be montonically decreaseing!! Then we will count the len or something liek that! IDK

1. Please note this yah


4.Something like that of how i drew it, please try to go through the 

5. time complecity
Prob will be O(N) as you will go through all the item once
O(N) you will have a stack thats about tis for space
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]: # If the current tmep is more than the last item you will pop\
                pop_index, pop_temp = stack.pop()
                len_days = i - pop_index
                res[pop_index] = len_days


            stack.append((i, temp))

        return res
 







