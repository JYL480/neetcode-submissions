"""

0. intuition?
- So othis would be similar, they can ask you do the letters etc
- They want to havee mathcing pairs. 
- This can be done with stack\
- This is when you want to process the top of the dat with the incoming one
- Which works beccause this is like a flower ts ??


1. What they want?
- They want to teturn a bool for this shit

3.  com0lpecity
O(N) for both

4. How to ?

"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_hash = {"(":")", "[":"]", "{": "}"}
                
        # Then we will have a stack is with what?
        for char in s:
            
            if stack and char not in char_hash:
                # Then we check ,meaing the char now is closing, see fi the the top matches
                top_char = stack[-1]
                corres_char = char_hash.get(top_char, None)

                if char == corres_char:
                    print(char, corres_char)
                    stack.pop()
                    continue
                else:
                    return False


            stack.append(char)

        if stack:
            return False
        else:
            return True













        