class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        res, i = 0, 0

        for c in word:
            j = keyboard.index(c)
            res += abs(i - j)
            i = j
        
        return res