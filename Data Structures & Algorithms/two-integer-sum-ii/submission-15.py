"""
0. ascending order, then having left and right works yah for 2 pointers
2 pointers method to be done in a single pass

1. What do they want
- You have to return a list whicih contaunes the index of the 2 numbers that add up to target
- The index is pos to 1 yah. 

.... Skip

4. Pattern
- Using 2 pointers from left and right, 
- if sum is more then r -= 1
if sum is lesser than +=1 
- , there is a while loop tho..



"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers) - 1
        

        while l < r:
            total_sum = numbers[l] + numbers[r]

            print(total_sum, target)
            # Here we will do the checiig 
            if total_sum == target and l != r:
                return [l+1,r+1]

            # THen here will be the condition to move forward again loh....

            if total_sum < target:
                l += 1 
            elif total_sum > target:
                r -=1


                









        