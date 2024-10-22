# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque()
        q.append(root)
        levels = []
        while len(q) > 0:
            n = len(q)
            curr = 0
            for i in range(n):
                p = q.popleft()
                curr += p.val
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
            levels.append(curr)

        levels.sort()
        return -1 if len(levels) < k else levels[-k]
