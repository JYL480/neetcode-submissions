"""
0. What is theinutiotion, 

- This is defiinitely a 2 pointer yah for this questioon, they want to you wto retrun the  max area given in the thingy 
- The thingy that is always limiting the area or volume of water will be the hehgiht of the bar
- So you will always mvoe the  shorteer  hegith of the bar
- Then each time you will cacluate the area
- They didnt ask you to return the index or what, we just want the area od water thats all!!!!!!

- THis has the same concept as the k blocks of water in teh enext question


skip 

4. 2 pointers
- You will continuously move the shorter bar 
- How would you claculate the area?
Will be the min(l, r) * width




"""





class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0 
        r = len(heights) - 1
        max_area = 0

        while l < r:

            area = min(heights[l], heights[r]) * (r - l)
            

            if heights[l] < heights[r]:
                l +=1

            else:
                r -=1

            max_area = max( area, max_area)
            print(max_area)
        return max_area
            






        
