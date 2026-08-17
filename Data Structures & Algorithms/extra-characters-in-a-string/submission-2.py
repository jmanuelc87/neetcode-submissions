class Node:
    def __init__(self):
        self.root = {}
        self.leaf = False
        self.length = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        temp = self.root
        k = 0
        for c in word:
            if c not in temp.root:
                temp.root[c] = Node()
                k += 1
            temp = temp.root[c]
        temp.leaf = True
        temp.length = k


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()

        for word in dictionary:
            trie.insert(word)

        def peek(i, cur):
            if i in cur.root and cur.root[i].leaf:
                return cur.root[i].length

            maximum = 0
            for k in cur.root.keys():
                if k in cur.root:
                    t = peek(k, cur.root[s[i]])
                    maximum = max(maximum, t)

            return maximum

        return peek(0, trie.root)
