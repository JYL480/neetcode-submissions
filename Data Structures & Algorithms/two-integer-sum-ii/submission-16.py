"""
0. They want to use return the index
- the index 1 ahs t o be small er and they canmot be equal to eahc other
- Converggin2 pointer 
- 

"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers) - 1

        while l <= r:
            t_sum = numbers[l] + numbers[r]

            if t_sum < target: #meaning that I can move up, i want something bigger
                l += 1
            elif t_sum > target: # Too big liao, ,have to move down, having it sorted helps!!!
                r -= 1
            elif t_sum == target and l!= r:
                return [l+1, r+1]

                









        