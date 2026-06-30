"""
0. How would you do it in a single pass?

Most of thetime we would to keep a monotonic stack. 
In this question we are doing based on timinng it takes to reach the targeet. if the timing is leser than thth eopt, means it will 
- It will intersect and join that fleet
- This will be a monotically increasing stack as well to do this in a single pass 

4. So I will have to sort first, why?
- Becuase I need to evaluate the nearest to the target first. 
Because this is a single lane carraige, meaning, the further will determin the fleeet
- Becuase it will be blockinng

- I will also create a monotonic increasing stack for this!!!
- which will store the time taken to reach the target ,
- Anything that is lesser than the time will not be addded to to the stack 
- Anything that is larger will be added because this means that it is suer slow and will not intersect 



"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_speed_dict = {}
        for i, num in enumerate(position):
            pos_speed_dict[num] = speed[i]
        # Then I will sort ts
        # Take note of the syntax yeah, there is ..items() here hor!!!!!!
        pos_speed_list = sorted(pos_speed_dict.items(), reverse = True)
        
        for tup in pos_speed_list:
            pos = tup[0]
            sp = tup[1]
            time = (target - pos) / sp
            
            if stack and time <= stack[-1]:
                continue
                

            stack.append(time)
        return len(stack)









        