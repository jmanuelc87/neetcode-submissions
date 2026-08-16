class TrieNode:
    def __init__(self):
        self.children = {}
        self.leaf = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.leaf = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()

        for w in wordDict:
            trie.addWord(w)
        
        def peek(i, path):
            if i == len(s):
                res.append(" ".join(path))
                return
            
            node = trie.root
            word = []

            for i in range(i, len(s)):
                char = s[i]
                if char not in node.children:
                    break
                
                word.append(char)
                node = node.children[char]

                if node.leaf:
                    path.append("".join(word))
                    peek(i+1, path)
                    path.pop()
        
        res = []
        peek(0, [])
        return res
