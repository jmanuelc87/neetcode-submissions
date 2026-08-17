class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        path = set()

        def dfs(k, l, i):
            if i == len(word):
                return True
            
            if (min(k, l) < 0 or
                k >= n or
                l >= m or
                word[i] != board[k][l] or
                (k,l) in path):
                return False
            
            path.add((k,l))
            res = (dfs(k + 1, l, i + 1) or 
                    dfs(k - 1, l, i + 1) or
                    dfs(k, l + 1, i + 1) or
                    dfs(k, l - 1, i + 1))
            path.add((k,l))
            return res

        for r in range(n):
            for c in range(m):
                if dfs(r, c, 0):
                    return True

        return False