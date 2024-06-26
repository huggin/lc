# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def f(p):
            if p is None:
                return
            f(p.left)
            nodes.append(p)
            f(p.right)

        f(root)

        def build(l, r):
            if l > r:
                return None
            m = l + r >> 1
            p = nodes[m]
            p.left = build(l, m - 1)
            p.right = build(m + 1, r)
            return p

        return build(0, len(nodes) - 1)
