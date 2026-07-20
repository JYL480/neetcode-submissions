"""
0. Hint, well it is still sorted, ascedning and they want in logn timining
- So its a different type of binary search 


4.  You need to how which to serach, youare in 2 segments which allows you to be 
- You need to figure out if you are in left or right
- get the min

- Note you if l < r, meaiing that we are in a sorted position and that you have to break 

"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)- 1

        min_val = float('inf')

        while l <= r:

            # Okay if somehow we landed in a sorted, then left will be the smallest, then break

            if nums[l] < nums[r]: # We are in a sorted
                min_val = min(min_val, nums[l])
                break
            
            mid = (l + r) //2

            # We check whether that value is smallest or ysing min

            min_val = min(nums[mid], min_val)


            # Now we check whehter we are left or right segment

            if nums[mid] >= nums[l]: # Means we are in left segment, we know that the right side will def be smaller
                l = mid + 1
            elif nums[mid] < nums[l]: # we are right side, then we have r = mid - 1, beacus the right of left is def larger mah 
                r = mid - 1
            
        return min_val


















