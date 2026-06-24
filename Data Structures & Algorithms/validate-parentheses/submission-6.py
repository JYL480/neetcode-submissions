"""
0. Lol i think i had this question in shoee and had to no clue how to do this. 
- Okay this is the stack one, Im guessing you ahve to pop from the front and  add the bacl?/

This one quite simple ig, just peek the last and the first element of teach and see

1. What does the question want?
- They want to return a bool to see if its being closed prop anot
- Have to be followed in a pair []. (). {}all these my be paired tgt


2. Edge cases
What are thee edge cases?
- When you have only 1 thing, then nreturn false

3. Niave?
- DK

4. Using a list stack for this hsit ,
you will peek the top thingy and look at the btoom, then you will popmove accorudingly??????????

5. Time c omplcity, 
O(N) bah, you just have to loop th elist for this




You have to understand the use of staack to contoniouly input and output things. 
in this question we are only will append the clodint bracket and will not append the closin b5rackets

"""


class Solution:
    def isValid(self, s: str) -> bool:
        # Not that stack has not to be empty then we do thec hecking for all the openinng brackets
        stack = []

        close_hash = {"}":"{", "]":"[", ")":"("}
        
        for char in s:

            if stack and char in close_hash:
                top = stack[-1]
                print(top)

                if stack and close_hash[char] == top:
                    stack.pop()
                else:
                    return False
            
            else:
               
                stack.append(char)
                print(stack)
        
        print(stack)
        if not stack:
            return True
        else:
            return False
                












        