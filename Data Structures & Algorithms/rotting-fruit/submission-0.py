class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        directions = [(1, 0), (-1,0), (0, 1), (0, -1)]
        fresh = 0
        steps = 0
        q = []
        visited = set()

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        while q:
            r, c, k = q.pop(0)

            steps = max(steps, k)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 1 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, k + 1))
                    fresh -= 1

        return steps if fresh == 0 else -1