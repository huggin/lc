# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0
        stack = []
        p = head
        while p:
            stack.append(p.val)
            p = p.next

        p = head
        while p:
            ans = max(ans, p.val + stack.pop())
            p = p.next

        return ans
