class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            
            if t in "+":
                stack.append(stack.pop() + stack.pop())
            elif t in "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t in "*":
                stack.append(stack.pop() * stack.pop())
            elif t in "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                op = int(t)
                stack.append(op)
        
        return stack[0]