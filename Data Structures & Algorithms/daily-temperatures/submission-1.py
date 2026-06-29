"""

0. Hmmmm, I guess you can have a stack, of when you have a warmer day, then keep adding until you have more than, 
- Thne pop and restart the process?

- Or you can 2 pointers this shit
- Okay so this is a monotonic stack type of question  question, 
YOu will create a sepearate stack to store the lesser temp , only when you haev larger temp then you will 
do the counting


1. WHat does thee q want?
- So they want you to return a list of int, which contains the number of days at the temp till it receives a ore
higher temp 

2. Edge cases?
- All the same? ->return a list of 0s

3. Naive
- You can do a nested for loop N^2

4. Pattern?/
- You will use a monotnoic decreaseing stack for this

"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]* len(temperatures)

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, i))
            else:
                while stack and temp > stack[-1][0]:
                    
                    stackT, stackI = stack.pop()
                    # If the now temp is more, then you will cal the no of days
                    res[stackI] = i - stackI
                
                stack.append((temp,i))

        return res


            
        
    










