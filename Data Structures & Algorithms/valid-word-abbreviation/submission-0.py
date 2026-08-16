class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l, r = 0, 0

        while l < len(word) and r < len(abbr):

            if word[l] == abbr[r]:
                l += 1
                r += 1
            elif abbr[r].isalpha() or abbr[r] == "0":
                return False
            else:
                sublen = 0
                while r < len(abbr) and not abbr[r].isalpha():
                    sublen = sublen * 10 + int(abbr[r])
                    r += 1
                l += sublen

        return l == len(word) and r == len(abbr)