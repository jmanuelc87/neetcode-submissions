class Node:
    def __init__(self):
        self.nodes = {}
        self.name = None
        self.leaf = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, folder: str):
        tmp = self.root
        paths = folder.split("/")
        n = len(paths)
        for path in paths:
            if path not in tmp.nodes:
                tmp.nodes[path] = Node()
                tmp.nodes[path].name = path
                tmp.nodes[path].leaf = False

            tmp = tmp.nodes[path]

        tmp.leaf = True

    def iter_remove(self):
        res = []

        def dfs(root, path):
            if root.leaf:
                res.append(path)
                return

            for kk in root.nodes.keys():
                tmp = "/" + root.nodes[kk].name
                dfs(root.nodes[kk], path + tmp)

        for key in self.root.nodes.keys():
            dfs(self.root.nodes[key], "")
        
        return res


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        box = Trie()
        for path in folder:
            box.add(path)
        
        return box.iter_remove()
