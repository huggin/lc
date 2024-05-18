# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def f(p):
            nonlocal ans
            if p is None:
                return 0, 0
            lf, ln = f(p.left)
            rt, rn = f(p.right)
            v = lf + rt + p.val
            cnt = ln + rn + 1
            ans += abs(v - cnt)
            return v, cnt

        f(root)
        return ans
