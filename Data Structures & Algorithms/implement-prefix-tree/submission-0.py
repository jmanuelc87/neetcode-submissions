class TreeNode:
    def __init__(self):
        self.childs = {}
        self.leaf = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        tmp = self.root

        for c in word:
            if c not in tmp.childs:
                tmp.childs[c] = TreeNode()
            
            tmp = tmp.childs[c]
        
        tmp.leaf = True

    def search(self, word: str) -> bool:
        tmp = self.root
        for c in word:
            if c not in tmp.childs:
                return False
            tmp = tmp.childs[c]
        return tmp.leaf

    def startsWith(self, prefix: str) -> bool:
        tmp = self.root
        for c in prefix:
            if c not in tmp.childs:
                return False
            tmp = tmp.childs[c]
        
        return True
        