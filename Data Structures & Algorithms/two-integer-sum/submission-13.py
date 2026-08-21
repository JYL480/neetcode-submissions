"""
0. Lets do this first, I was not able to think this question in my head 
- ofc for a 2 sum question we need to have a hs_map for this yah

4. And eccrythign will be done in a single pass
- If the comp is not in the thing then you will add to the hash map



"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}

        
        for i, num in enumerate(nums):
            comp = target - num

            if num not in hs:
                hs[num] = i
            
            # print(num, )
            if comp in hs and i != hs[comp]:
                return [hs[comp], i]
