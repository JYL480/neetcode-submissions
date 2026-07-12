"""
0. What gives it away?
- That this is in ascending order
- And that it is log(m*n) meaning you have logM + logn, what is the complexity 
- Likely will be binary search twice!!!!


4. You have to do binary search twice, do it properly with special segmnetation in 
rows cols then top and down typeshit yeah
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top, down = 0, len(matrix)-1
        chosen = 0 

        while top <= down:
            mid = (down + top) //2


            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                down = mid - 1

            else: 
                chosen = mid 
                # Why it wont stop? Because 
                break # Lol becasue in the other things you have a return statement LOL, so just hav eto note 
                
        print(chosen)

        l , r = 0, len(matrix[0]) - 1

        while l <= r:
            mid = ( l + r ) //2

            if matrix[chosen][mid] < target:
                l = mid + 1
            elif matrix[chosen][mid] > target:
                r = mid - 1
            else:
                return True
        return False

                     
