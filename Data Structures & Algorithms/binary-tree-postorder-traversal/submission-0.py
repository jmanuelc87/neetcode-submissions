# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        self.postOrder(root, values)
        return values

    def postOrder(self, root, values):
        if root is None:
            return
        
        self.postOrder(root.left, values)
        self.postOrder(root.right, values)

        values.append(root.val)
