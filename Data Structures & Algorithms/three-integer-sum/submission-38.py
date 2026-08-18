"""
0. THis is a 2 pointer question, ubt then it will be a 2 pointner once you get your thingy
- They want to prevent any duplicate, 
- So you have to check kfor first element uplicate
- Then after that you have to check for the 2nd element duplicate

- So it the first and first prev
- And then it is the 2nd and 2nd prev, this is very impt yah


4. umm

I think its n logn or n^2



"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []

        nums = sorted(nums)

        for i in range(len(nums) - 2):

            l = i + 1
            r = len(nums) - 1
             # So here we need tp pcheck the first dup, which is the first and its first prev
             # ( -1, -1, 0, 1 ) I order to not have (-1 0 1) 2 of this, this will do it

            if i>0 and nums[i-1] == nums[i]: 
                continue

            # then it would be the l and r 2 pointers yah 

            while l<r:
                t_sum = nums[i] + nums[l] + nums[r]

                if t_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                    r -= 1
                elif t_sum > 0:
                    # meaing then we need to be smaller, 
                    r -= 1
                else:
                    l +=1
        return res

                














            
     