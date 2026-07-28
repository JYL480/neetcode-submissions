"""
0. immedite intution
- Sorted, rotated and sorted!!! FK
- This is using binary search


4. Finding the min only
- I think its like that......


"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_val = float('inf')



        while l <= r:
            if nums[l] < nums[r]: # Edge case if its aldy sorted lol
                min_val = min(min_val, nums[l])
                break
            
            mid  = (l + r) //2 
            min_val = min(nums[mid], min_val)


            if nums[mid] >= nums[l]: #This means that we are in the left sgeement 
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid - 1
            
        return min_val
            
            















