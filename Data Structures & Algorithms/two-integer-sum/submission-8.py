"""
0. 2 sum, immediately you know that they want to have hashmap witht he commp bah

1. what they want?
return the index yah of the 2 that equal to each other 
- the indices cannot be the sam
e

4. Pattern?
- I will prob use a hashmap for this!!
- Put the complement in thash map and do it in a single pass
- In the hash i will put in the comp in the key and the index in the value?





"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}
        res = []
        
        for i, num in enumerate(nums):
            comp = target - num


            if comp in hash_map and i!= hash_map[comp]:
                return [hash_map[comp], i]

            hash_map[nums[i]] = i

