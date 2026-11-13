class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        cache = {}

        def dfs(alice, i, M):
            if i == n:
                return 0

            if (alice, i, M) in cache:
                return cache[(alice, i, M)]

            res = 0 if alice else float("inf")
            total = 0
            for x in range(1, 2 * M + 1, 1):
                if i + x > len(piles):
                    break
                total += piles[i + x - 1]
                if alice:
                    res = max(res, total + dfs(not alice, i + x, max(M, x)))
                else:
                    res = min(res, dfs(not alice, i + x, max(M, x)))

            cache[(alice, i, M)] = res
            return res

        return dfs(True, 0, 1)
