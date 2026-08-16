class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[0] * n for i in range(n)]
        total = 0

        def dfs(r):
            nonlocal total
            if r == n:
                total += 1
                return
            
            for c in range(n):
                if self.isSafe(r, c, board):
                    board[r][c] = 1
                    dfs(r + 1)
                    board[r][c] = 0

        dfs(0)
        return total
    
    def isSafe(self, r: int, c: int, board: list[list[int]]):
        row = r - 1
        while row >= 0:
            if board[row][c] == 1:
                return False
            row -= 1
        
        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == 1:
                return False
            row -= 1
            col -= 1
        
        row, col = r - 1, c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == 1:
                return False
            row -= 1
            col += 1
        
        return True
