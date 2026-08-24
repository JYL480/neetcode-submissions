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

        ch = {'(': ')', '{': '}', '[':']'}


        for char in s:

            # Okay then then here will be all the thingy left whic are the clsoed bracket
            if stack and char not in ch:

                top_char = stack[-1]
                corres_char = ch.get(top_char, None)

                if char == corres_char:
                    print(char, corres_char)
                    stack.pop()
                    continue
                else:
                    return False

            stack.append(char)

        if not stack:
            return True
        else:
            return False
















        