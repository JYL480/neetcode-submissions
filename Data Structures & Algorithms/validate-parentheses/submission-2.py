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




"""


class Solution:
    def isValid(self, s: str) -> bool:
        s_list = list(s)
        print(s_list)
        cor_hash = {}
        cor_hash["}"] = "{"
        cor_hash[")"] = "("
        cor_hash["]"] = "["
        open_set = "({["
        close_set = ")}]"
        
        stack = []
        
        for char in s_list:
            # print(type(char))
            if char in close_set:
                if stack and stack[-1] == cor_hash[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False











        