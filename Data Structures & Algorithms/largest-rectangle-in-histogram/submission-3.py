"""
0. to do this in a single pass you prb have to create something new
- Creaate a new array or something, But what woul dbe this new array to store?
- You would store a monotonic increasing stack which 
- Then you can do in single pass to check the area of the shit?
- What is the popping factor?
- When the next item is less than, then you will pop and update the max area????
- The elements left in the stack will be able to extend right all the way to the end 
- When we pop we will check the curretnt area and all the way to the lefT??????





"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = [] # (index, height)
        max_area = 0
        for i, num in enumerate(heights):
            start = i
            while stack and stack[-1][1] > num:
                index, height = stack.pop()
                max_area = max(max_area, (i - index) * height)
                start = index 
            stack.append((start, num))
        print(max_area)

        print(stack)

        for i, h in stack:
            max_area = max(max_area, h* (len(heights) - i))

        return max_area








        