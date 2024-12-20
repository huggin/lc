# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        def f(p1, p2, level):
            if p1 is None:
                return
            if level == 1:
                p1.val, p2.val = p2.val, p1.val
            f(p1.left, p2.right, 1 - level)
            f(p1.right, p2.left, 1 - level)

        f(root.left, root.right, 1)
        return root
