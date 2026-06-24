"""
0. Same concept, because we are tyring to find the max numerb of spots or the count ,then the limiting factor 
-Which changes the max count will be the smaller hegiht, Same concetp yah. So this will be condition to move l or r
- We can also use prefix and suffix for this shit 


skip

4. we will do the suffix and prefix fisrt for fun yhea 


- Because in this question, we need to find the that index befrore the min 

- How do we calcaulte the max a

- this is not th right method,  ebcos this uese count....
- max is not the use ofo count  i think?

- THe next method will be to use the 2 pointers for this yah
-  Just take note that the you dont need to care too much if thay index stores wahter
- The calculate of that storing of water will take care for you
- Becuase if ti cannot stroe water it will eiither be 0 or negative number yeah. 

- In the 2 pointer solution, waht is happending, that you wwwe walways calcute and move the smaller thingy



"""


class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height)-1
        count = 0
        max_l, max_r = height[l], height[r] 

        while l<r:
            if max_l < max_r:
                l +=1 
                # You will get the new max hieight, for the next iteration, but now you move to the new one, 
                # We need so how much water can be added 
                max_l = max(max_l, height[l])
                count += max_l - height[l]
            else:
                r -=1
                max_r = max(max_r, height[r])
                count+=max_r - height[r]
        return count


        




        
