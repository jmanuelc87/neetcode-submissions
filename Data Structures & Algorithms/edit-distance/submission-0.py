class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        def dfs(i, j):
            if i == n:
                return m - j
            if j == m:
                return n - i

            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)

            res = 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))

            return res

        return dfs(0, 0)
