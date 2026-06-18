"""

0. First intition
- You will create a hash map , dict to store the values. Then see if there is the complement within the hash map 

1. What does the q wants?
- It wants to get the index addition that equals to teh target value. 
- The indices cannot be the same yah 
- You will return the list with the index. Smallest one first yah

2. edge case?
    - Only 2 of the same nymebrs

3. naive?
nested for loop to tget the target. 
Bottleneck = O(n^2)

4. Pattern or what to do?
    - You will store the value in a hash map, which stores the value and the index
    - If the complement number in the hash map, then get the index value loh

5. Time complexiyt?
Will be O(N) same with sapce


"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}
        res = []

        for num_index in range(len(nums)):
            num_hash[nums[num_index]] = num_index


        for num_index in range(len(nums)):
            complement = target - nums[num_index]
            if complement in num_hash and num_index != num_hash[complement]:
                return [num_index, num_hash[complement]]


# What c

