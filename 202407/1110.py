# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        ans = []
        td = set(to_delete)

        def f(p, parent, is_left, is_root):
            if p is None:
                return
            if p.val in td:
                if parent:
                    if is_left:
                        parent.left = None
                    else:
                        parent.right = None
                f(p.left, None, True, True)
                f(p.right, None, False, True)
                return
            elif is_root:
                ans.append(p)
            f(p.left, p, True, False)
            f(p.right, p, False, False)

        f(root, None, True, True)
        return ans
