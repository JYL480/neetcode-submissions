"""
0. Searching iwth binary search, How do we do thisyah?

- Same conectp if wea re in the left or right segment, but now got more nuance

4. I thinnk thats the pattern as well, 
you need to whether you are in the left or right segmet


"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l + r)//2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]: # means we are in left segment, treat m largest, l smallest
                if nums[mid] < target or nums[l] > target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[r] < target or nums[mid]> target:
                    r = mid - 1
                else:

                    l = mid + 1
            

        
        print(mid)
        
        return -1