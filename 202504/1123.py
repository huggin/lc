# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth = [-1] * 1001

        def f(p, v):
            if p is None:
                return
            depth[p.val] = v
            f(p.left, v + 1)
            f(p.right, v + 1)

        f(root, 0)
        ma = max(depth)
        cnt = sum(1 for c in depth if c == ma)

        self.ans = None

        def f2(p):
            if p is None:
                return 0
            left = f2(p.left)
            right = f2(p.right)
            if left + right == cnt:
                if self.ans is None:
                    self.ans = p

            if left + right != 0:
                return left + right
            if depth[p.val] == ma:
                if cnt == 1:
                    if self.ans is None:
                        self.ans = p
                return 1
            return 0

        f2(root)
        return self.ans
