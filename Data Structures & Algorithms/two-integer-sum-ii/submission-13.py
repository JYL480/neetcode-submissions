"""
0. First intuition:
- Urm yeah there ill me dup ig
- But you will return the index that sums up to the target value. 
My return a list of the indexes
- index return must be in ascending order
- THis will mean 2 pointers i think


1. Return a list 

2. Edge acases
- When there are the same nymber? - Just ahve to take note?
- IDK 
- have to take note of negative num

3. Naive?
- Im guesing nested for again. .....


bottle neck = O(N^2) bad

4. Pattern?
- 2 pointer 
- Where a main pointer will poknter to the curre 
- The other will move. 
- THis will be in a O(N^2) if im not wrong yah
- LIke that loh



"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            
            if numbers[left] + numbers[right] == target:
                return [left+1, right +1]
            if numbers[left] + numbers[right] > target:
                # I will move the right nymber down
                right-=1
                continue
            elif numbers[left] + numbers[right] < target:
                left+=1








        