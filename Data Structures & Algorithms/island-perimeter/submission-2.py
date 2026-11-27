class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 1
            
            if (i, j) in visit:
                return 0


            visit.add((i, j))
            perim = dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1)

            return perim

        perim = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    perim += dfs(i, j)
        
        return perim