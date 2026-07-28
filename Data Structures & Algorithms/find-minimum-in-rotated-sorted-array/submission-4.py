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

        if nums[l] < nums[r]: # Edge case if its aldy sorted lol
            return nums[l]

        while l < r:
# the minimum MUST be in the right half!
            mid = (l + r)//2

            if nums[mid] > nums[r]:
                l = mid + 1
            # Otherwise, the minimum is either at mid or in the left half
            else:
                r = mid

        return nums[l]
            















