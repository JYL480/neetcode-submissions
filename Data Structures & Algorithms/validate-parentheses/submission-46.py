"""
0. This question keeps pissing  me off bruv ,Try again 
- First instinct, you knomw this is a general stack question, where if there still things inside aftet the single pass ,then you will return false etc...

"""


class Solution:
    def isValid(self, s: str) -> bool:
        ch = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []

        for char in s:
            
            # Rmb when dealing we input stringn ts, we will prcess and then add

            if stack and char in ch:
                top = stack[-1]
                if stack and top == ch[char]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)

        return not stack





















        