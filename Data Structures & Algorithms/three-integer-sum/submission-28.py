"""
0. Intuition?
Right using 2 pointes .
- I think also you will have to srot will be better oso?
- nlogn or i guess it will be nested loh




1. what do they want?
they want you to return a list of list 

- 3 elements that add up to 0 
- Note the duplciations yah 
- First check for initiali duplicates
- Then the final duplications for the next


4. Pattern would be that you have to use 2 pointers for htis
- with a lot of duplication checks for the 1st and 2nd thingy




"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums = sorted(nums)

        
        for i, num in enumerate(nums):
            l = i+1
            r = len(nums)-1

            if i > 0 and num == nums[i-1]:
                continue
            
            # Thats why we continue with this shit
            while l <r :
                t_sum = nums[l] + nums[r] + num
                if t_sum ==0 :
                    res.append([nums[l], nums[r], num])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1

                if t_sum>0:
                    r -=1
                elif t_sum<0:
                    l+=1
        return res
                    










        