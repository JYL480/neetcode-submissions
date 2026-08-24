"""
0. Do this stupid question again????
- LOL IDK, should i do trapping rainwater?? I think i should hor, if you want to test out your binary search tchinques right????

- This was donw with the thingy idk fkkk i want to kms!!!!

- Anyway what is this this is i immediately this is a stack question yah!!! How do you know!!
- because we are doing the 
- Anyway you know the gist


4. What is the pattern?
- You will store the inside bracket first, onece the inside bracket is done, then you will check with their corresponding sets to check whether is its correct or not!!! LOL
- If the stack is not empty, then you will return false else True

5. Complexity?
- O(N) for space
O(N) - for time as well ig

"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', '}': '{', ']': '['}

        # Note that youi are processing first then add the char to the stack yuah 

        for char in s:
            if char in matching:
                if stack and stack[-1] == matching[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack













        