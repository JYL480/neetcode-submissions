"""
0. What is binary search, is not like you are parsing, but youare searching whtn you have a 
target
- So int this case we can find what segment to use which is either left or right 


1. Return the inices in logn time


4.


"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        
        while l <= r:
            # checl first if middle is good?
            m = (l + r) //2

            if nums[m] == target:
                return m

            if nums[m] >= nums[l]: #left sorted seg
                if nums[l] > target or nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            else: #rigth osrted segemtn

                if nums[m] > target or nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1
        return -1
                

