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


"""


class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * (len(height))
        max_l = 0

        for i, num in enumerate(height):
            # You will add in the height inside here loh 
            prefix[i] = max_l
            max_l = max(num, max_l)

        suffix = [0] * len(height)
        max_r = 0 
        for i in range(len(height) -1, -1, - 1):
            suffix[i] = max_r
            max_r = max(max_r, height[i])
        

        # Okay now its gucci
        count = 0
        for i, num in enumerate(height):
            cur_count = min(suffix[i], prefix[i]) - num
            print(cur_count)
            if cur_count >0:
                count += cur_count
            
        return count

        




        
