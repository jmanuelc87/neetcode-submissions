# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = [root.val]
        self.bisectRight(root.right, res)
        return res

    def bisectRight(self, node, res):
        if node is None:
            return
        
        res.append(node.val)
        self.bisectRight(node.right, res)