# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = []
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            cl = 0
            for i in range(n):
                p = q.popleft()
                cl += p.val
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
            level.append(cl)

        q.append(root)
        root.val = 0
        k = 1
        while q:
            n = len(q)
            for i in range(n):
                p = q.popleft()
                if p.left and p.right:
                    temp = level[k] - p.left.val - p.right.val
                    p.left.val = temp
                    p.right.val = temp
                    q.append(p.left)
                    q.append(p.right)
                elif p.left:
                    temp = level[k] - p.left.val
                    p.left.val = temp
                    q.append(p.left)
                elif p.right:
                    temp = level[k] - p.right.val
                    p.right.val = temp
                    q.append(p.right)
            k += 1

        return root
