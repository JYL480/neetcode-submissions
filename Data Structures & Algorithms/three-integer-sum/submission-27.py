"""
- So we have to check the first 2 items of the dupicat yeah, because if the first 2 are the saem, last will be sa, e
- Porb will have to sort to use the 2 pointer methods
- They want to return a list of list yeah 



"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        res = []

        for i,num in enumerate(nums):

            # DO the first initioal checcker here yah 
            if i > 0 and num == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l <r:
                t_sum = nums[l] + nums[r] + num
                # print(t_sum)

                if t_sum == 0:
                    # Then you will append to the list an dmove to check if the first thingy has ither numbers
                    res.append([nums[l], nums[r], num])

                    l+=1
                    while l <r and nums[l] == nums[l-1]:
                        l+=1

            # Then moving condition
                if t_sum <0:
                    l+=1
                    
                elif t_sum >0:
                    r-=1
            # print(res)
        return res



        