"""
0. Intuition 
- Yeah so this is a min stsack question
- havev a monotoniic stack or min stack such that the top is always the min???

1. What do they want
- Create different functions all in O(1) time

4. What is the pattern 
- Push shoyuuld be easy
get min - They didnt mention to create anotehr stack right
- So we can create a new stack to store the min, and then change pop accordingly leaving the top to be the min
- IDK we will 
- How do you maintain a min stack?? Such that the top is always a min? HMMMMM



5. Complexity
- Time - O(1)
spsace- O(N) bah  


"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_value = float("inf")

    def push(self, val: int) -> None:
        # We will have to push 2, note that the otehr min stack will have to be the top
        self.stack.append(val)
        # NO the min_stack will append the min at that level yah, it will not change that much!!!
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_value = min(val, self.min_stack[-1])
            self.min_stack.append(self.min_value)


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:

        return self.min_stack[-1]
        
