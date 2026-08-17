# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = [0]
        self.dfs(root, d, 0, 0)
        return d[0]
    
    def dfs(self, root, d, l, r):
        if root is None:
            return 0

        ml = max(l, self.dfs(root.left, d, l + 1, r))
        mr = max(r, self.dfs(root.right, d, l, r + 1))

        d[0] = max(d[0], ml + mr)

        return max(l, r)