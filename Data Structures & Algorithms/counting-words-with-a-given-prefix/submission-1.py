class TrieNode:
    def __init__(self):
        self.array = {}
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word: str):
        temp = self.root
        for char in word:
            if char not in temp.array:
                temp.array[char] = TrieNode()

            temp.array[char].count += 1
            temp = temp.array[char]

    def prefix(self, pref: str):
        temp = self.root
        for char in pref:
            if char in temp.array:
                temp = temp.array[char]
            else:
                return 0
                
        return temp.count


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        data = Trie()
        for word in words:
            data.add(word)

        return data.prefix(pref)
