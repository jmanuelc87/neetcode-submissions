class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)

        for i, word in enumerate(words):
            m = len(word)
            for j in range(m):
                if j >= n or i >= len(words[j]) or words[j][i] != word[j]:
                    return False


        return True