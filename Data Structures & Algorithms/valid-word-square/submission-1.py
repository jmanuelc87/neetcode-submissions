class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        result, n = True, len(words)

        if n == 1:
            return False

        for i, word in enumerate(words):
            m = len(word)
            for j in range(m):
                if words[j][i] != word[j]:
                    result = False
                    break


        return result