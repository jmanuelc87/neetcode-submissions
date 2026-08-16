class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, current):
            if len(current) == k:
                res.append(current.copy())
                return
            
            for j in range(i, n):
                if j > n:
                    continue
                current.append(j + 1)
                dfs(j + 1, current)
                current.pop()
        
        dfs(0, [])
        return res