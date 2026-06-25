class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        op = "+-*/"
        stack = []
        result = 0
        for i, char in enumerate(tokens):
            print(char)
            if char in op:
                sec_op = int(stack[-1])
                stack.pop()
                first_op = int(stack[-1])
                stack.pop()
                if char == "+":
                    result = first_op + sec_op
                    stack.append(result)
                    
                elif char == "-":
                    result = first_op - sec_op
                    stack.append(result)
                    
                elif char == "*":
                    result = first_op * sec_op
                    stack.append(result)
                    
                elif char == "/":
                    result = int(first_op / sec_op)
                    stack.append(result)
                
                print(result, stack)
            
            else:
                stack.append(int(char))
                
        
        return stack[-1]
        

