class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}

        def dfs(i, j):
            if i > j:
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            even = (j - i) % 2 == 0
            left = piles[i] if even else 0
            right = piles[j] if even else 0

            cache[(i, j)] = max(dfs(i + 1, j) + left, dfs(i, j - 1) + right)
            return cache[(i, j)]

        total = sum(piles)
        alice_score = dfs(0, len(piles) - 1)
        return alice_score > (total - alice_score)
