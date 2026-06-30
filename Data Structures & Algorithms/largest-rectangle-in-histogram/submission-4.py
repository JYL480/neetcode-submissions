"""
0. Question quite tough yah
- Draw the fokcin thiingy out, 
- Same thing we are dealing with monotonically increasing stack
- Why we want to have increasing stack, because then at the end of the looop
- With the indices, the remainign element can go from tthat index to the very end at the height





"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0 
        # index = 0 

        for i, num in enumerate(heights):
            
            start = i
            # I will apend the index and hieght in the stackk yeah
            while stack and num < stack[-1][1]:
                index, cur_height = stack.pop()

                area = cur_height * (i - index)
                max_area = max(max_area, area)
                # I will need to
                start = index
            
            stack.append((start, num))
        print(max_area)

            
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area








        