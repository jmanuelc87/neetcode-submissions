class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        rot = [[0] * n for _ in range(m)]

        for i in range(n):
            for j in range(n):
                rot[j][n - 1 - i] = matrix[i][j]

        for i in range(n):
            for j in range(m):
                matrix[i][j] = rot[i][j]
