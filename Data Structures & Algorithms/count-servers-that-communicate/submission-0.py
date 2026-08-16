class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        res = 0
        n, m = len(grid), len(grid[0])

        for r in range(n):
            r_sum = sum(grid[r])
            if r_sum <= 1:
                continue
            res += r_sum
            for c in range(m):
                if grid[r][c]:
                    grid[r][c] = -1
        
        for c in range(m):
            c_sum = unmarked = 0
            for r in range(n):
                c_sum += abs(grid[r][c])
                if grid[r][c] > 0:
                    unmarked += 1
                elif grid[r][c] < 0:
                    grid[r][c] = 1
            if c_sum >= 2:
                res += unmarked
        

        return res