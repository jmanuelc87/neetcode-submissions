class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        cache = [[None] * 2 for _ in range(n)]

        def dfs(i, alice):
            if i >= n:
                return 0

            if cache[i][alice] is not None:
                return cache[i][alice]

            res = float("-inf") if alice == 1 else float("inf")
            score = 0
            for j in range(i, min(i + 3, n)):
                if alice == 1:
                    score += stoneValue[j]
                    res = max(res, score + dfs(j + 1, 0))
                else:
                    score -= stoneValue[j]
                    res = min(res, score + dfs(j + 1, 1))
            
            cache[i][alice] = res
            return res


        r = dfs(0, 1)

        if r == 0:
            return "Tie"

        return "Alice" if r > 0 else "Bob"