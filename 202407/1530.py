# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0

        def f(p):
            if p is None:
                return []
            if p.left is None and p.right is None:
                return [0]

            l = f(p.left)
            r = f(p.right)
            for a in l:
                for b in r:
                    if a + b + 2 <= distance:
                        self.ans += 1
            return [1 + a for a in l] + [1 + b for b in r]

        f(root)
        return self.ans
