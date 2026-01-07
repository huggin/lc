# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        vals = []

        def f(p):
            if p is None:
                return 0
            v = p.val + f(p.left) + f(p.right)
            vals.append(v)
            return v

        tot = f(root)
        ans = 0
        for v in vals:
            ans = max(ans, (tot - v) * v)
        return ans % MOD
