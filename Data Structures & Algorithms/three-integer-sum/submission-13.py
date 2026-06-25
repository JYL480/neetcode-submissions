"""
0. Array question, and likely will be using 2 pointers, with a singular anchor at the start
- Hmm if you want to use 2 pointers you prob woudl have to sort this so that I know right side will not be 
anythign etc......
- I think this question will be O(N^2) bops
- Also this makes sense, if you are sorted, the first element will immediately determine the order you have aldy
- So if you have - 1 at the start, aso check that the next also isnt a duplicate

1. What they want?/
- They want to return all the all the elements of the indeices that sum up to 1
- Cannot have duplicates. 

-

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # nlogn
        
        res = []



        for i, num in enumerate(nums):
            l = i + 1
            r = len(nums) - 1

            # Rmb to check for uplcateicat at first yeah i think
            if i > 0 and nums[i-1] == num:
                continue

            while l <r :
                t_sum = nums[l] + nums[r] + num 

                if t_sum == 0:
                    res.append([nums[l], nums[r], num])
                    l +=1
                    while l<r and nums[l-1] == nums[l]:
                        l+=1


                # now we need to know what is the condition for moving l or r. 
                # The factor will be more than or less 0
                if t_sum > 0: #Meaning too large you will move r down
                    r -= 1
                elif t_sum < 0:
                    l+=1
                    
                # Here can have dup as well for the second item ig, 3rd will not because obviously it is the last
                # So you have to take not of the second thingy as well, as if the first 2 are the same, the last item will def be the same 
            
                    



        return res

        