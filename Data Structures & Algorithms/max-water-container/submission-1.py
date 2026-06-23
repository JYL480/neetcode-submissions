"""

0. 2 pointers again, where you will take note of the max lenght and value/mag of the elements in teh list
- My inutition is that there will be 2 constant pointers that will keep tabs on maxH and maxW yeah. 

1. What they want?
- return the volume or an integer which gives the max amount of value. 


2. Edge cases?
When all the value in list are 0, meaning cannot store waters return 0

3. Naiev?
nested for loop ig to track which is the max
Bottleneck = O(N^2)

4. Pattern?
- you have 2 pointers in a single pass which tracks the max h and w. 
- if you hvae the maxH and maxw thne you can return the max volume at the end of the day 



"""





class Solution:
    def maxArea(self, heights: List[int]) -> int:

        pointer_l = 0
        pointer_r = len(heights) - 1
        max_h , max_w = 0, 0
        max_v = 0

        # The height will be the min yah
        while pointer_l < pointer_r:
            cur_w = (pointer_r +1)- (pointer_l +1) 
            
            cur_h = min(heights[pointer_l], heights[pointer_r]) 
           
            cur_v = cur_w * cur_h
            print("w, h, v",cur_w, cur_h, cur_v) 

            max_v = max(cur_v, max_v)
            print(max_v)

            # i cannot keep blindly moving them yah
            
            if heights[pointer_l] >= heights[pointer_r]:
                print("ASD")
                pointer_r -=1
                
            if heights[pointer_l] < heights[pointer_r]:
                print("ASDA")
                pointer_l +=1
            # pointer_r-=1
            # pointer_l +=1
            
        return max_v
            






        
