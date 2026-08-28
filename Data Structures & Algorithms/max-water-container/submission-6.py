"""
0. Find the containwer with th emost wayter????
- HOw do you find?
- What is first inutiotion??
- Well from what i know this is a 2 pointer question
- Which is converging, note that we dont have to sort this because then how do we move??
- IDK 

1. They want to return the area of` the max water


4. Pattern?
- Wee need to know how to calculae the area
which is 
(r - l ) x min(l,r)  
like this?

What is the moving condition??
- We will move the shorter L or R yah, because that is the limiting factor right 
- We want to get max area, but the limiting is the L or R, will keep shifring the shorter and update area

- w4e just leepmoving ah

"""





class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1

        max_area = 0 
        
        while l<r:
            
            left_h = heights[l]
            right_h = heights[r]
            max_area = max(max_area, (r-l) * min(left_h, right_h))

            if left_h<= right_h:
                l += 1
            else:
                r -=1

        return max_area














        
