# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        def find(p, s, path):
            if p is None:
                return -1
            if p.val == s:
                return 0
            l = find(p.left, s, path)
            r = find(p.right, s, path)
            if l == -1 and r == -1:
                return -1
            if l == 0:
                path.append("L")
            else:
                path.append("R")
            return 0

        path1 = []
        path2 = []
        find(root, startValue, path1)
        find(root, destValue, path2)

        while path1 and path2 and path1[-1] == path2[-1]:
            path1.pop()
            path2.pop()

        return len(path1) * "U" + "".join(reversed(path2))
