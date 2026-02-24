# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def f(p, curr):
            nonlocal ans
            if p is None:
                return
            if p.left is None and p.right is None:
                ans += curr * 2 + p.val
            f(p.left, curr * 2 + p.val)
            f(p.right, curr * 2 + p.val)
        f(root, 0)
        return ans
