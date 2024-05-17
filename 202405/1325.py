# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        def f(p):
            if p is None:
                return None
            left = f(p.left)
            right = f(p.right)
            if left is None and right is None and p.val == target:
                return None
            p.left = left
            p.right = right
            return p

        p = f(root)
        return p
