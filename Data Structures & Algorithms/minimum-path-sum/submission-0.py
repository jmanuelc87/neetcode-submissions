class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cache = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if i >= m or j >= n:
                return float("inf")

            if i == m - 1 and j == n - 1:
                return grid[i][j]

            if cache[i][j] != -1:
                return cache[i][j]

            cache[i][j] = grid[i][j] + min(dfs(i + 1, j), dfs(i, j + 1))

            return cache[i][j]

        return dfs(0, 0)
