"""
0, Okay you have to redo this shit yah, you just need to know how to do so hor 

- WHat does htis mean?
- You need tonow that yoj must sort this shit 
- And that you need to know for loop in a certain range yah
- also, that you have l  and r to always move yah


"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)

        res = []

        for i in range(n - 2): # why - 2 because we need to have 2 left and r pointer left!! because we are chooding the first item in here
            if i >0 and nums[i] == nums[i-1]:
                continue
            
            l = i  + 1
            r = n - 1

            while l < r:
                t_sum = nums[i] + nums[l] + nums[r]

                if t_sum == 0:
                    res.append([nums[l], nums[i], nums[r]])

                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                    r -=1

                elif t_sum >0 : #can afford to move down
                    r -=1 
                elif t_sum < 0:
                    l += 1
        return res