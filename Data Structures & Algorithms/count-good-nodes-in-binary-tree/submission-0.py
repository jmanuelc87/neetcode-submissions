# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.path(root, root.val)
    
    def path(self, node, maxVal):
        if node is None:
            return 0
        
        res = 1 if node.val >= maxVal else 0
        maxVal = max(maxVal, node.val)
        res += self.path(node.left, maxVal)
        res += self.path(node.right, maxVal)
        return res
