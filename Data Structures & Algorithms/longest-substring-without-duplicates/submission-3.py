class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxWindow = 0, 0
        a = set()

        for r in range(len(s)):
            while s[r] in a:
                a.remove(s[l])
                l += 1
            a.add(s[r])            
            maxWindow = max(maxWindow, r - l + 1)

        return maxWindow