"""
0. I know this aldu 2 pointers., 
- But i guess, it can be 3?

1. They want to return a list of list which containes the values of the indices. 
- INside will contain the values, and they cannot be duplicated yah
- The list must be distinct, cannot have duplicates yah
- The values in the list list can be duplicate but the indices cannot be repeated


2. EDge cases:
- Urm nothing sum to zero?
- 

3. Naive?
- nested 3 for loops?
- LOL 

4. Pattern?
- 3 pointers?
- It will be n^2, cannot be more that than that liao


"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

    # Okay i sort of had it. 
    #Just use the sum logh
        res = []
        nums = sorted(nums)
        
        for i, num in enumerate(nums):
            if i >0 and nums[i -1] == num:
                continue
            
            # Then we will do the 3 pionter ish?
            l = i + 1
            r = len(nums) - 1
            while l < r:
                t_sum = nums[l] + nums[r] + num 

                if t_sum < 0 :
                    l +=1
                elif t_sum > 0:
                    r -=1
                else:
                    if t_sum == 0:
                        res.append([nums[l], nums[r], num])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                    

                # print(res)

        return res
                 

            

        