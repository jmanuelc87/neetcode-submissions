class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {c:k for k,c in enumerate(order)}

        def compare(word):
            return [order[c] for c in word]

        return words == sorted(words, key=compare)