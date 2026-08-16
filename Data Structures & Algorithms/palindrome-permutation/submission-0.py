class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = defaultdict(int)

        for c in s:
            freq[c] += 1

        res = 0
        for k, v in freq.items():
            res += v % 2
        
        return res <= 1