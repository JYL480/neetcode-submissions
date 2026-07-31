"""
0. Okay we are using binary search yah
- How do you do it, what is the time complexiy?
- Time complexity
n/2^k = 1

Theu will find the value k = 
log2n = This is the time complexity which is gucci 


skip

4. Pattern?
- Yes binary search you should know the pattern
- Why this works because it is aldy sorted yah!!! HTis iit he reason hor!!!

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: # Always have to be less than or equal yah!! THis is the case hor 

        #     mid = l + (l - r) //2 # Because there can be overflow, but in this case should be okay 
            mid = (l + r) // 2
            print(mid)

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else: 
                print(mid)
                return mid
            
        return -1
            
            




