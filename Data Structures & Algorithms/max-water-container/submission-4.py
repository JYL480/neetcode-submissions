"""
0.
- THis is a 2 pointer question
- You will move the left or the right thingy
- So you will need to know which to move, either to move the left or right
- How do i know? You will move the shorted ehgihter one, because that is the ljiting factor bah


1, What do they want?
- They want to largest area, You will return 
- The area, an iint yah 


skip

4. pattern?
- This will be a 2 pointer question
- either move left or right based on a condition
- Each time we will claculagte the area loh
- How do you calcualte the area r - l + 1 x min(l,r) value 


"""





class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0 
        r = len(heights) - 1
        max_area = 0
        
        for index, height in enumerate(heights):

            area = (r - l ) * min(heights[l], heights[r])
            
            
            max_area = max(area, max_area)

            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1 
            
        return max_area








        
