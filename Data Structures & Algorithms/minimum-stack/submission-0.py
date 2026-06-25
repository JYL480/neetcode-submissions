"""
0. stack question LOL

1. What do othey want?
- Want you to create functions bascially a  stack which has a getMinn()
- Should be simple enoiught i THINKK!!

2. edge?
-IDK LOL

3. naive?
- Non?

4. pattern?
- Note that all the functions have to be done in O(1) time yeah 
- 

"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [float('inf')]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min_stack[-1]:
           self.min_stack.append(val)
        elif val > self.min_stack[-1]:
            # We will swap places\
            
            self.min_stack.append(self.min_stack[-1])

        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        # A seperate_list
        # Maybe every time i append i cehcl so that the thingy is always order to be placed on the top?
        # The min will be alwasy 
        print(self.min_stack)
        return self.min_stack[-1]





