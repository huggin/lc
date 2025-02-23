# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        def f(pre, i1, j1, post, i2, j2):
            if i1 > j1:
                return None
            if i1 == j1:
                return TreeNode(pre[i1])
            k = pre.index(post[j2 - 1])
            p = TreeNode(pre[i1])
            p.left = f(pre, i1 + 1, k - 1, post, i2, k - 2 - i1 + i2)
            p.right = f(pre, k, j1, post, k - 1 - j1 + j2, j2 - 1)
            return p

        return f(preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1)
