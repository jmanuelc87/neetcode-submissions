class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = defaultdict(int)
        n = len(s)

        for i, c in enumerate(s):
            if c not in freq:
                freq[c] = i
            else:
                freq[c] = n
        
        res = n
        for f in freq:
            res = min(res, freq[f])

        return -1 if res == n else res