# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        data = []
        
        def f(p):
            if p is None:
                return
            f(p.left)
            data.append(p.val)
            f(p.right)
        
        f(root)
        ans = 100001
        for i in range(1, len(data)):
            ans = min(ans, data[i]-data[i-1])
        
        return ans
