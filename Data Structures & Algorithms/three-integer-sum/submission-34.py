"""
3sum question is a classic yah
- Bacisllay you ones you got the first poihter, then you will move thepointer after 
- This one has a lot of duplicates so you need to note how to deal with them bah'
- What do you mean by duplicate 
0. so if the first and then second is the same, then you will move
- and now that you gor your first one then you will move on the find the next few that are invikded....

- This shit is 2 poibter, the 2 pointners will be after findin the first number

4. Fk we wiilll see how it is i guess
- Its impotant to know what is teh duplicated we are lookin godr?????
- We are looking the first duplciated and
and 2nd duplciate 
- Cause we can 1 duplcate aldy, the we cannot have another 1 with the same as we will get the same answere
- Then within the 2nd and its previous dupicate has to be correct as well!!

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            
        res = []

        nums = sorted(nums)

        for i, num in enumerate(nums):
            l  = i + 1
            r = len(nums) - 1

            # We have to check for the first duplicate and its previous first 
            if i> 0 and nums[i-1] == num:
                continue

            while l < r: # stanadrd 2 poinnter converginn yah 
                t_sum = num + nums[l] + nums[r]

                if t_sum ==0:
                    res.append([num, nums[l], nums[r]])
                    # here we will have to deal with dup for the second one oso

                    l += 1
                    while l<r and nums[l-1] == nums[l]:
                        l += 1 # Becuase this would be cleared yah, 

                elif t_sum>0:
                    #Meaing too big, have to mvove down r
                    r -= 1

                elif t_sum<0:
                    l += 1

        return res
            


