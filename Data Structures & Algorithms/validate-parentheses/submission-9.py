"""
0. What is this? 
- This is clearly a stack question =
- We want to see if the inside and outside match yah 
- Valid parenthesis
- So you will add until the opening one, then after you conpare the closing
- If yes match, the pop
- Only when the stack is empty then you will return true


1. What do they want?
- They want to return boool , 
- Check whether the string is valid or not

skip


4. for this we have to use a stack fo rhtis uyeah


"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        char_set = {"}": "{", "]":"[" , ")": "("}

        for char in s:
            
            if stack and char in char_set:
                if char_set[char] == stack[-1]:
                    stack.pop()
                    print(stack)
                    
                elif char_set[char] != stack[-1]:
                    print(stack)
                    return False
            else:
                stack.append(char)
        
            # print(stack)

        if stack: return False
        else:
            return True
     
                












        