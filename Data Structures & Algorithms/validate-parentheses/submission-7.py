"""
0. Maybe an intuition for this will be 
- If you are lookingn a string or list, can you moving through the indices, 
- If I see the latest item in teh list, what should I do???
- FIFO Ts????
- Or what I want to undo back step??? IDK
- You are keeping track of the current state???

1. What does the question wnant?
- Return bool 
- If there is an ordered closing and opendinng braxket pairs. 

skip

4. obviously I will be using stack for this
- In this case, I will just add the openig bracket insiides, , I will not append the closing braket yea
- Then I will pop 
- Will  be true if there is nothing left loh

"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close_bra = {"}":"{",")":"(", "]":"["}
        # I will check if in above to not append and then check

        for char in s:
            print(char)
            if stack and char in close_bra:
                # So if the top is in close_bra corresponding then pop, if not return false
                top = stack[-1]

                if top == close_bra[char]:
                    stack.pop()
                else:
                    return False
            else:
                print("A")
                stack.append(char)

        if stack:
            return False
        else:
            return True
     
                












        