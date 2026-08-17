class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(1, len(s) - 1):
            left, right = s[0:i], s[i:-1]

            zeroes = [1 for c in left if c == "0"]
            ones = [1 for c in right if c == "1"]

            res = max(res, sum(zeroes) + sum(ones))
        
        return res
