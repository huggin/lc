# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            new_node = TreeNode(val, root)
            return new_node

        def doit(node, d):
            nonlocal val, depth

            if not node:
                return

            if d == depth:
                left = node.left
                right = node.right
                new_left = TreeNode(val, left=left)
                node.left = new_left
                new_right = TreeNode(val, right=right)
                node.right = new_right
            else:
                doit(node.left, d + 1)
                doit(node.right, d + 1)

        doit(root, 2)
        return root
