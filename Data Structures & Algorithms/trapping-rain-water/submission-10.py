"""
0. Same concept, you can either prefix and post fixmethod, 
- Or will just move the limiting hegiht as we want to find the max rain water to be stored. 


4. Pattern?

How do we calucalte the area?
area = min(left or right) - value 
- This is it, 
but when are doing min will be the one that is being moved aldy, 




"""


class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0 
        r = len(height) - 1
        count = 0 
        max_l, max_r = height[l], height[r]

        


        

        while l < r:            
            if max_l <= max_r:
                l +=1
                max_l = max(max_l, height[l])
                print( max_l - height[l])
                count += max_l - height[l]
                
                
            else:
                r -=1
                max_r = max(max_r, height[r])
                print(max_r - height[r])
                count+=max_r - height[r]
       
        return count
            


  
        




        
