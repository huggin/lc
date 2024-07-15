# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d = {}
        children = set()
        for p, c, l in descriptions:
            if p not in d:
                d[p] = TreeNode(p)
            if c not in d:
                d[c] = TreeNode(c)
            children.add(c)
            if l == 1:
                d[p].left = d[c]
            else:
                d[p].right = d[c]
        
        for p, _, _ in descriptions:
            if p not in children:
                return d[p]
        return None
