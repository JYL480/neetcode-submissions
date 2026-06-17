"""
0. Has duplicate? What is my immediate intuition?
    - Create a seen dict, if yes then return t etc...

1. Rephase?
    - If the element in the list appear more than once, then you will return true, else false

2. Edge case?   
    - Appear only once, all once, then false
    0 No nymber at all?- false ig

3. Nive?
    - nested for loop to count ig
    bottle neck? - o(n^2)

4. pattern
    - Will create a seen dict and count. 
    - If seen > 1, then return true or fal;se


5. Time complexity
    - O(N) for the counting ig
    - Will be good, like a hash map O(1)
    - Spave will be O(N)


"""


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            seen[num] = 1 + seen.get(num, 0)
        
        for k,v in seen.items():
            if v >1:
                return True

        return False







