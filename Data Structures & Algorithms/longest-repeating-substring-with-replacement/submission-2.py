class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, longest, maxf = 0, 0, 0
        repeat = defaultdict(int)

        for r in range(len(s)):
            repeat[s[r]] += 1
            maxf = max(maxf, repeat[s[r]])

            while (r - l + 1) - maxf > k:
                repeat[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest