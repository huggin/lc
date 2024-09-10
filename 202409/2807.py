# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        p = head
        while p and p.next:
            v = gcd(p.val, p.next.val)
            q = ListNode(v, p.next)
            p.next = q
            p = q.next
        return head
