class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if (i < n and j < m and obstacleGrid[i][j]) or (i >= n or j >= m):
                return 0

            if i == n - 1 and j == m - 1:
                return 1

            if cache[i][j] != -1:
                return cache[i][j]

            cache[i][j] = dfs(i, j + 1) + dfs(i + 1, j)

            return cache[i][j]

        return dfs(0, 0)
