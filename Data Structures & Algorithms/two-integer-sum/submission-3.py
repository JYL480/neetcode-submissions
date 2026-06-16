"""
1. There are 2 numbers within the list that when added tgt will satisfy the target number
    - I want you to return the index of those numbers
    - There will be a valid pair no matter wad yah

2. Edge cases?
    - Only 2 numbers in the list? 
        - Just return those 2 numbers

3. Naive?
    - We can do a nested for loop
    Bottleneck: bad complexity n^2

4. Pattern we can think of?
- I will create a hash map for this, check if the remaining value is in the hash map where the value will be the index
- O(N), time will be the size of the list
- O(N) space will be the same 


"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Very simple querstion yah
        seen = {}
        index_list = []

        for index in range(len(nums)):
            seen[nums[index]] = index

        for index in range(len(nums)):
            remaining = target - nums[index]

            if remaining in seen and seen[remaining]!= index:
                    return [index, seen[remaining]]

