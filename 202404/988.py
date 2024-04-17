# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = "|"

        def f(p, prefix=[]):
            if p is None:
                return
            if p.left is None and p.right is None:
                prefix.append(p.val)
                self.ans = min(
                    self.ans, "".join(chr(ord("a") + c) for c in reversed(prefix))
                )
                prefix.pop()
                return
            prefix.append(p.val)
            l = f(p.left, prefix)
            r = f(p.right, prefix)
            prefix.pop()

        f(root)
        return self.ans
