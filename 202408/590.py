"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        ans = []

        def f(p):
            if p is None:
                return
            for c in p.children:
                f(c)
            ans.append(p.val)

        f(root)
        return ans
