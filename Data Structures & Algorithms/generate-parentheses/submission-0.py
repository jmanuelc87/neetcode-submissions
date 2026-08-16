class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def backtrack(N, M):
            if N == M == n:
                result.append("".join(stack))
                return
            if N < n:
                stack.append("(")
                backtrack(N + 1, M)
                stack.pop()
            if M < N:
                stack.append(")")
                backtrack(N, M + 1)
                stack.pop()

        backtrack(0,0)
        return result