"""
0. Oh hashmap ts??

1. What they want?
- Rteurn bool if there are repeated nums

4. pattern

"""


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num not in seen:
                print(num)
                seen[num] = 1 + seen.get(num, 0)
            else:
                return True
        return False


