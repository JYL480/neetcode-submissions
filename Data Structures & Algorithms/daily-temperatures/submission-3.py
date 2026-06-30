"""
0. How many days in between which until there a day with higher temp, 

- You want to do this in a single pass. This aslo means you will only add to the somehting a lists
- When it is only increasing????
- You will use monotonic stack yeah. 

- Huh wdym by monotonic stack, so you dont have to do 1 by 1 luh, 
You can do by indices yeah

1. What does the question want?
- Return a list of in their indices wwiht the number days, int


2. 

3. nested for loop for naive

4. Pattern?

- So the tracking al lwill be done in the stack, the for loop will be done in a sinngle pass

O(N)
O(N)
for both time and space


"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            # Will append both temp and index?
            # We will implement a strictly monotic stack
            # So there will be while loop 
            while stack and temp > stack[-1][1]:
                index, cur_temp = stack.pop()
                res[index] = i - index

            
            stack.append((i, temp))
        return res 






            
        
    










