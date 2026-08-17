class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False

        def dfs(i, j, current, picked):
            if current == word:
                res = True
                return

            for k in range(i - 1, i + 2):
                if k >= 0 and k < len(board):
                    for l in range(j - 1, j + 2):
                        if l >= 0 and l < len(board[k]):
                            if not picked[k][l]:
                                picked[k][l] = True
                                current += board[k][l]
                                dfs(k, l, current, picked)
                                picked[k][l] = False

        dfs(0,0,"",[[False] * len(board[0])] * len(board))

        return res

