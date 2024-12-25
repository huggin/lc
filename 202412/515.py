# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            ma = float("-inf")
            for _ in range(n):
                p = q.popleft()
                ma = max(ma, p.val)
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
            ans.append(ma)
        return ans
