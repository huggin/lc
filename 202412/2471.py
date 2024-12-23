# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        ans = 0
        while q:
            n = len(q)
            a = []
            for i in range(n):
                p = q.popleft()
                a.append([p.val, i])
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)

            b = sorted(a)
            for i in range(n):
                if b[i][0] != a[i][0]:
                    a[i], a[b[i][1]] = a[b[i][1]], a[i]
                    a[b[i][1]][1] = b[i][1]
                    ans += 1
        return ans
