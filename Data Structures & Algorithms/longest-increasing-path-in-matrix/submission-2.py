class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        indegree = [[0] * m for _ in range(n)]

        # indegree calculation
        for r in range(n):
            for c in range(m):
                for dr, dc in directions:
                    if (
                        0 <= r + dr < n
                        and 0 <= c + dc < m
                        and matrix[r + dr][c + dc] < matrix[r][c]
                    ):
                        indegree[r][c] += 1

        # retrieve the first layer or all nodes with degree zero
        q = deque()
        for r in range(n):
            for c in range(m):
                if indegree[r][c] == 0:
                    q.append([r, c, 1])

        # depth breath search
        longest = 0
        while q:
            r, c, l = q.popleft()

            longest = max(longest, l)

            for dr, dc in directions:
                if 0 <= r + dr < n and 0 <= c + dc < m and matrix[r + dr][c + dc] > matrix[r][c]:
                    indegree[r + dr][c + dc] -= 1
                    if indegree[r + dr][c + dc] == 0:
                        q.append([r + dr, c + dc, longest + 1])

        return l
