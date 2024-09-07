# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def f(h, p):
            if h is None:
                return True
            if p is None or h.val != p.val:
                return False
            return f(h.next, p.left) or f(h.next, p.right)

        self.ans = False

        def f2(p):
            if p is None:
                return
            if f(head, p):
                self.ans = True
                return
            f2(p.left)
            f2(p.right)

        f2(root)
        return self.ans
