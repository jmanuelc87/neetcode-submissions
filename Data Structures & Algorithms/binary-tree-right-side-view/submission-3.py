# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, node, depth, res):
        if node is None:
            return
        
        if len(res) == depth:
            res.append(node.val)
        
        self.dfs(node.right, depth + 1, res)
        self.dfs(node.left, depth + 1, res)


