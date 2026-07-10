"""
0. ascending order
- If even in the array 2D it still sorted then very strong signal or binary searhc 
- With log base 2 mn thingy

1. What they want?
- They want you to return a bool, if the target is whein the matrix!!!!

2. 

3. Naive?
Nest for ig

4. Pattern?

"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # We just have to do it twice loh

        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows - 1

        while top <= bot:
            row = (top + bot) //2

            if matrix[row][-1] < target: # IF the largetstvalue in that row is bigger than target then I move top down
                top = row + 1
            elif matrix[row][0] > target: # If the smallest value in that row is smaller than tha target then its this row or below
                bot = row - 1
                
            else:
                break
        if not top<=bot:
            return False


        row = (top + bot) //2

        l = 0 
        r = len(matrix[row]) - 1

        while l <= r:
            mid = (r + l )//2

            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        return False

