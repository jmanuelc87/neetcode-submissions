"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack = []
        res = []

        stack.append(root)

        while len(stack) > 0:
            el = stack.pop()

            if el and el.children:
                for child in el.children:
                    stack.append(child)

            res.append(el.val)
        
        return res[::-1]