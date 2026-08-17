class Node:
    def __init__(self):
        self.root = {}
        self.leaf = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        temp = self.root
        for c in word:
            if c not in temp.root:
                temp.root[c] = Node()
            temp = temp.root[c].nodes
        temp.leaf = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()

        for word in dictionary:
            trie.insert(word)

        i = 0
        tmp = trie.root
        for c in s:
            if c in tmp.root:
                tmp = tmp.root[c]
                i += 1
            else:
                break

        return len(s) - i
