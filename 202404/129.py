# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def f(p, v):
            if p is None:
                return

            nv = v * 10 + p.val
            if p.left is None and p.right is None:
                self.ans += nv
            f(p.left, nv)
            f(p.right, nv)

        f(root, 0)
        return self.ans
