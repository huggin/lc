# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        d = {}
        if root:
            q.append((root, 1))
        while q:
            n = len(q)
            for i in range(n):
                curr, level = q.popleft()
                if level not in d:
                    d[level] = curr.val
                else:
                    d[level] += curr.val
        
                if curr.left:
                    q.append((curr.left, level + 1))
                if curr.right:
                    q.append((curr.right, level + 1))
            
        ans = -1
        for k, v in d.items():
            if ans == -1 or v > d[ans]:
                ans = k

        return ans
