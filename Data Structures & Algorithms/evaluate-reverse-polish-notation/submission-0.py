class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            
            if t in "+":
                x = stack[-2] + stack[-1]
                stack.append(x)
            elif t in "-":
                x = stack[-2] - stack[-1]
                stack.append(x)
            elif t in "*":
                x = stack[-1] * stack[-2]
                stack.append(x)
            elif t in "/":
                x = stack[-1] // stack[-2]
                stack.append(x)

            try:
                op = int(t)
                stack.append(op)
            except:
                pass
        
        return stack[-1]