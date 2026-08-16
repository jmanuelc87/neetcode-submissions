# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        self.dfs(stack)
        return root

    def dfs(self, stack):
        while len(stack) > 0:
            root = stack.pop(-1)

            if root is not None:
                stack.append(root.left)
                stack.append(root.right)

                tmp = root.left
                root.left = root.right
                root.right = tmp