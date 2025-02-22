# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        a = []
        n = len(traversal)
        cnt = 0
        i = 0
        while i < n:
            if traversal[i] != "-":
                j = i
                while j < n and traversal[j] != "-":
                    j += 1
                a.append((int(traversal[i:j]), cnt))
                cnt = 0
                i = j
            else:
                cnt += 1
                i += 1

        def f(i, j):
            if i == j:
                return TreeNode(a[i][0])

            p = TreeNode(a[i][0])
            cnt = 0
            for k in range(i + 1, j + 1):
                if a[k][1] == a[i][1] + 1:
                    cnt += 1
                    right = k
            if cnt == 2:
                p.left = f(i + 1, right - 1)
                p.right = f(right, j)
            elif cnt == 1:
                p.left = f(i + 1, j)
            return p

        return f(0, len(a) - 1)
