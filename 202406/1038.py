# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        p = root
        st = []
        curr = 0
        while p or len(st) > 0:
            if p is None:
                p = st.pop()
                p.val += curr
                curr = p.val
                p = p.left
            else:
                st.append(p)
                p = p.right

        return root
