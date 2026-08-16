class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r, c = 0, 0, 0
        res = []
        
        while l < len(word1) or r < len(word2):
            if c == 0 and l < len(word1):
                res.append(word1[l])
                c = 1 if r < len(word2) else 0
                l += 1
            elif c == 1 and r < len(word2):
                res.append(word2[r])
                c = 0 if l < len(word1) else 1
                r += 1

        return "".join(res)