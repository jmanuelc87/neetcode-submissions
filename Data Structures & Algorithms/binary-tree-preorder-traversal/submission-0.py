# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        self.preOrder(root, values)
        return values

    def preOrder(self, root, values):
        if root is None:
            return
        
        values.append(root.val)

        self.preOrder(root.left, values)
        self.preOrder(root.right, values)