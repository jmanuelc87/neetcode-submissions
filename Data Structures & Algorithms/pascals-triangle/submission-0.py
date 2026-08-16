class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        i = 1
        for r in range(numRows):
            row = []
            for c in range(i):
                if c == 0 or c == i - 1:
                    row.append(1)
                else:
                    row.append(triangle[r - 1][c - 1] + triangle[r - 1][c])
            triangle.append(row)
            i = i + 1
        return triangle