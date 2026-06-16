"""

Understand
- Understand the question first. 

- What is the input and output, break it down slowly

- Think about edge cases?

Brainstorming
- Naive solution?
- Bottle Neck identification?
- What patterns do you see?
- Complexity?


Implementation
- If cannot do see solutions and watch video
- Ask whether you needed help, if so repeat this question again. 

Reflection
- Ask how did I do this etc..

"""


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        
        for num in nums:
            if num in seen: 
                return True
            else: 
                seen.add(num)
        
        return False

# What is the complexity of this?
# Space O(N), N = len(num) O(N)
        
"""
Understand
- See within the array if there are more then 1 number!
Inut is a list, output is boolean t or f. 
- Should be simple entough

- Any edge case? When there nothing? Return false ig

Brain storming
- I think can use 2 pointers for this. Would not be O(N^2) complextiy compared to the naive solution
- Will compare if both are equal until they meet at the center 

- OMFG right, for unique numbers you can use set() LOL completely forgot aobut this 
isalpha 
isnum is a thing btw
 
 - We will create a hash table for this. THis hash table will be to then check if we have seen the nymber
 - O(1) time to check


Reflection: 
- Oh wow I totally forgot about set(), i need to figure out the syntax for set()
- set(nums)
- or you can set().adds, you can add them tgt yah just take note. 
- Hmm the use of the hash table to check works for me. O(1) time for checking right. 


"""









