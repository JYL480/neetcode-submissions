"""
SKIP

4. What is the pattern??
- WE want a monotonic stack to differentiate how we allow the bar to either move extend to left or right
- If after the for loop, and the nodes left in the monotonic stack remains, these nodes can extend all the way to thr right
- Because the bars are in increasing order. 
- Elif its not monotically incraeseing, the abvoe will not be true, but here we know the left is true, 
- As we can extend to the left, thus the cur starting index will the popped one. 



"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, num in enumerate(heights):

            # What is the correct while logic 
            #[i-1] this is the  prev
            min_index= float('inf')
            start = i # LOL using this

            while stack and stack[-1][1] > num: # if the previous is larger than curr, then pop
                index, cur_height = stack.pop()
                
                length = (i - index)
                max_area = max(max_area, (cur_height * (length)))

                start = index

        
            stack.append((start,num))
            

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area
                







        