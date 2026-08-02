"""

0. THis will be a warm up. To warm my brain power!!!

1. WHat they want?
- to return a list of the index which equates the targe

4. Prob have to use a hash map for this 
- With the correspond comp

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}

        for i, num in enumerate(nums):
            comp = target - num


            if comp in hs and i != hs[comp]:
                return [hs[comp], i ]
            # I will always add the current number inside

            hs[num] = i