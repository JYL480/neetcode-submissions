"""
SKIP

4. What is the pattern??
- WE want a monotonic stack to differentiate how we allow the bar to either move extend to left or right
- If after the for loop, and the nodes left in the monotonic stack remains, these nodes can extend all the way to thr right
- Because the bars are in increasing order. 
- Elif its not monotically incraeseing, the abvoe will not be true, but here we know the left is true, 
- As we can extend to the left, thus the cur starting index will the popped one. 

- rmbthat we need a monotonic stack for this shit


"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # REDOOOOO
        stack = [] # this is a monotoic stack yah , inside will store a tuple which will contain the index and hiehgt

        max_area = 0

        for i, height in enumerate(heights):
            start = i 

            while stack and stack[-1][1] > height:# Here is for the popping
                # Meaning we will have to ppo and do somehting 
                # Note that poping will return you the tuple value yah 
                index , pop_height = stack.pop()

                max_area = max(max_area, (pop_height * (i-index)))

                # I will have to change the index of the next added with the pop height
                start = index

            stack.append((start, height))


        
        for i, h in stack:

            max_area = max(max_area, (len(heights) - i) * h)
        return max_area
        




        