class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        cache = [None] * n
        cache[n - 1] = True

        def dfs(i):
            if cache[i] is not None:
                return cache[i]

            if i >= n:
                return True

            cache[i] = False
            end = min(i + maxJump + 1, n)
            for j in range(i + minJump, end):
                if s[j] == '0' and dfs(j):
                    cache[i] = True
                    break

            return cache[i]

        return dfs(0)