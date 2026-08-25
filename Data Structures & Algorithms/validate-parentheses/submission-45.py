"""
0. Brother this is an easy quesiton hor!!!
This is stack question
- You will always handle, process first than you append okay, this is sequence you should always look for yah!!!!
- Take note hor!!!
- That's about it hor


4. A general stack

"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ch = { ")" : "(", "]" : "[", "}" : "{" }

        # the kwy will be in the key ho 
        for char in s:

            # Okay I will process, meaning if my char in ch now meaning its closing then we will de
            if stack and char in ch:
                if stack and stack[-1] == ch[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
                print(stack)

        

        return not stack























        