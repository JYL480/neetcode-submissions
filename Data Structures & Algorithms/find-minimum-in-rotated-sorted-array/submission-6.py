"""
0. We will do this again yah
- THis wants to us to find in logn and it is sorted so thats good YAY

"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        min_val = float('inf')

        while l <= r:
            
            # Edge case, if we somehow that whole thingis sorted left most will be the smallets
            if nums[l] < nums[r]:
                min_val = min(min_val, nums[l])
                print(l, r)
                break
            
            mid = (l + r)//2

            # We will do the thingy here

            min_val = min(nums[mid], min_val)

            if nums[mid]>= nums[l]:
                l = mid + 1
            elif nums[mid] <nums[l]:
                r = mid - 1
            
        
        return min_val














