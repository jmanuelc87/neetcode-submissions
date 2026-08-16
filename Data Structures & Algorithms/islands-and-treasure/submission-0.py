class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        N, M = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        def bfs(r, c):
            q = [(r, c, 0)]
            visit = [[False] * M for _ in range(N)]
            visit[r][c] = True

            while q:
                r, c, k = q.pop(0)
                if grid[r][c] == 0:
                    return k
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M and not visit[nr][nc] and grid[nr][nc] != -1:
                        visit[nr][nc] = True
                        q.append((nr, nc, k + 1))
            return INF
        
        for r in range(N):
            for c in range(M):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)