"""

0. Do for funsies LOL
Retur the indexes which equal to target


"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hahs map yah 
        hs = {None:None}

        for i, num in enumerate(nums):
            comp = target - num

            # the if condition here
            if comp in hs and i != hs[comp]:#Not the same index
                return [hs[comp], i]
            hs[num] = i

