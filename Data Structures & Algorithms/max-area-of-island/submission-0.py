class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        max_area = 0
        visit = set()

        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0 or (r, c) in visit:
                return 0
            
            visit.add((r,c))

            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        for r in range(R):
            for c in range(C):
                max_area = max(max_area, dfs(r, c))
        
        return max_area