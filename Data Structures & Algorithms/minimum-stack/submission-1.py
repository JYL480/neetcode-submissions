"""
0. wHAT DO THEY wnat?
All functioms will be O()

- They want to have all the functions as above and all lhas to be in O(1) timing yah

4. This is def a stack questions LOH

- But how do you getMin() in o(1) time?
- I will create another stack, where each elements in their indices will store
- The min value at the point

"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # so when im pushing, i iwll  push the min stack here??
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        elif self.min_stack and val < self.min_stack[-1]:
            self.min_stack.append(val) 
        elif self.min_stack and val >= self.min_stack[-1]:
            self.min_stack.append(self.min_stack[-1])
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
    
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]





