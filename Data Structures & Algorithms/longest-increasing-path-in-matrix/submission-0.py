class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        cache = {}

        def dfs(i, j, prev):
            if min(i, j) < 0 or i >= n or j >= m or matrix[i][j] <= prev:
                return 0

            if (i, j, prev) in cache:
                return cache[(i, j, prev)]

            res = 1
            for di, dj in directions:
                res = max(res, 1 + dfs(i + di, j + dj, matrix[i][j]))

            cache[(i, j, prev)] = res
            return res

        longest = 0
        for r in range(n):
            for c in range(m):
                longest = max(longest, dfs(r, c, float("-inf")))

        return longest
