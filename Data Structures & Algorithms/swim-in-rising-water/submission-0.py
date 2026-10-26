class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = []
        matrix_cost = [[float("inf")] for _ in range(len(grid[0]))] * len(grid)

        print(matrix_cost)

        return -1