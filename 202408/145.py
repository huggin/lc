# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def f(p):
            if p is None:
                return
            f(p.left)
            f(p.right)
            ans.append(p.val)

        f(root)
        return ans
