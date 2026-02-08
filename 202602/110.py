# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanced_height(self, p):
        if not self.ans:
            return 0
        if p is None:
            return 0
        
        left = self.balanced_height(p.left)
        right = self.balanced_height(p.right)
        if left > right + 1 or right > left + 1:
            self.ans = False
            return 0
        return max(left, right) + 1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.balanced_height(root)
        return self.ans
