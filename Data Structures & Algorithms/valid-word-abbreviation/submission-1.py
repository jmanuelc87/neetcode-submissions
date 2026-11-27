class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        m, n = len(word), len(abbr)
        i = j = 0

        while i < m and j < n:
            if abbr[j] == '0':
                return False
            
            if word[i] == abbr[j]:
                i, j = i + 1, j + 1
            elif abbr[j].isalpha():
                return False
            else:
                s = 0
                while j < n and abbr[j].isdigit():
                    s = (s * 10) + int(abbr[j])
                    j += 1
                i += s
        
        return i == m and j == n