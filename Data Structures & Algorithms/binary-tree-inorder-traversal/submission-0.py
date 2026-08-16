# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        self.inOrder(root, values)
        return values
    
    def inOrder(self, root, values):
        if root is None:
            return
        
        self.inOrder(root.left, values)

        values.append(root.val)

        self.inOrder(root.right, values)