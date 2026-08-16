class Node:
    def __init__(self):
        self.children = {}
        self.leaf = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str):
        tmp = self.root
        for c in word:
            if c not in tmp.children:
                tmp.children[c] = Node()
            tmp = tmp.children[c]
        
        tmp.leaf = True
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.insert(w)
        
        n, m = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= n or c >= m or (r, c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.leaf:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r,c))


        for r in range(n):
            for c in range(m):
                dfs(r, c, trie.root, "")

        return list(res)
