# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def f(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None or p.val != q.val:
                return False
            return (
                f(p.left, q.left)
                and f(p.right, q.right)
                or f(p.left, q.right)
                and f(p.right, q.left)
            )

        return f(root1, root2)
