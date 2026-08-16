class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op in "+":
                stack.insert(0, stack[0] + stack[1])
            elif op in "C":
                stack.pop(0)
            elif op in "D":
                stack.insert(0, stack[0] * 2)

            try:
                x = int(op)
                stack.insert(0, x)
            except:
                pass

        print(stack)
        return sum(stack)