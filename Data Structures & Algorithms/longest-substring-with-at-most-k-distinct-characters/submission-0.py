class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l, maxSize, n = 0, 0, len(s)
        counter = defaultdict(int)

        for r in range(n):
            counter[s[r]] += 1

            while len(counter) > k:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l += 1

            maxSize = max(maxSize, r - l + 1)

        return maxSize
