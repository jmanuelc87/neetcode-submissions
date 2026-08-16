# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = [root]
        score = 0

        while queue:
            el = queue.pop(0)

            if el.val >= low and el.val <= high:
                score += el.val
            
            if el.left:
                queue.append(el.left)
            
            if el.right:
                queue.append(el.right)

        return score