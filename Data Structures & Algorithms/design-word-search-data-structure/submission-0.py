class Node:
    def __init__(self):
        self.childs = {}
        self.leaf = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        tmp = self.root
        for c in word:
            if c not in tmp.childs:
                tmp.childs[c] = Node()
            tmp = tmp.childs[c]
        tmp.leaf = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.childs.values():
                        if child is not None and dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.childs:
                        return False
                    cur = cur.childs[c]
            return cur.leaf

        return dfs(0, self.root)