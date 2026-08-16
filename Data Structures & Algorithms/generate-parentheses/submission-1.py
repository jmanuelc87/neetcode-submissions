class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, stack = [], []

        def dfs(O, C):
            if O == C == n:
                res.append("".join(stack))
                return
            if O < n:
                stack.append("(")
                dfs(O + 1, C)
                stack.pop()
            if C < O:
                stack.append(")")
                dfs(O, C + 1)
                stack.pop()

        dfs(0,0)

        return res