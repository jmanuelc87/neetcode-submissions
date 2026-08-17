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
            if i == len(s):
                return 0

            if i < len(s) and s[i] in cur.root and cur.root[s[i]].leaf:
                return cur.root[s[i]].length

            if s[i] in cur.root:
                return peek(i + 1, cur.root[s[i]])
            else:
                return 0


        k = 0
        count = 0
        while k < len(s):
            count += peek(k, trie.root)
            k += 1

        return len(s) - count