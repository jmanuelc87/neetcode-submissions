class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > 26:
            return 0

        l, res = 0, 0
        rep = defaultdict(int)

        for r in range(len(s)):
            rep[s[r]] += 1

            while rep[s[r]] > 1:
                rep[s[l]] -= 1
                l += 1
            
            if r - l + 1 == k:
                res += 1

                rep[s[l]] -= 1
                l += 1

        return res