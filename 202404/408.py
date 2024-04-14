# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def f(p, flag=True):
            if p is None:
                return
            if p.left is None and p.right is None:
                if flag:
                    self.ans += p.val
            f(p.left, True)
            f(p.right, False)

        f(root, False)
        return self.ans
