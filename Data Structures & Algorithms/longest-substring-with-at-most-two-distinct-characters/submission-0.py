class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l, res = 0, 0
        seen = defaultdict(int)

        for r in range(len(s)):
            seen[s[r]] += 1

            while len(seen) > 2:
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    seen.pop(s[l])
                l += 1
            
            res = max(res, r - l + 1)

        return res