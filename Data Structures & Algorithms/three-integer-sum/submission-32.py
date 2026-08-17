"""
3sum question is a classic yah
- Bacisllay you ones you got the first poihter, then you will move thepointer after 
- This one has a lot of duplicates so you need to note how to deal with them bah'
- What do you mean by duplicate 
0. so if the first and then second is the same, then you will move
- and now that you gor your first one then you will move on the find the next few that are invikded....

- This shit is 2 poibter, the 2 pointners will be after findin the first number

4. Fk we wiilll see how it is i guess
- 

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        # Im pretty sure that this needs to be sorted for this work\

        nums = sorted(nums)

        for i, num in enumerate(nums):
            
            l = i + 1
            r = len(nums) - 1

            # What does this mean?
            # This is for the intinital duplcaite Ig, 
            if i > 0 and nums[i-1] == num:
                continue

            # What is the 2 pointers

            while l<r:
                t_sum = nums[l] + nums[r] + num

                if t_sum == 0:
                    res.append([num, nums[l], nums[r]])

                    l += 1
                    # Then you will have a while loop to check for the rest
                    while l<r and nums[l] == nums[l - 1]:
                        l += 1

                elif t_sum > 0:
                    # Meaning that it is too bug, ther right has to come down
                    r -= 1
                elif t_sum <0:
                    l += 1
        return res

                



    


















        