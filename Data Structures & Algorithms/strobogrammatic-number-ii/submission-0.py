class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        pairs = [
            ["0", "0"],
            ["1", "1"],
            ["6", "9"],
            ["8", "8"],
            ["9", "6"],
        ]

        def dfs(n, final_len):
            if n == 0:
                return [""]
            
            if n == 1:
                return ["0", "1", "8"]
            
            prev = dfs(n - 2, final_len)

            current = []

            for p in prev:
                for pr in pairs:
                    if pr[0] != "0" or n != final_len:
                        current.append(pr[0] + p + pr[1])

            return current
        
        return dfs(n, n)