# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head
        p = head
        n = 0
        while p is not None:
            n += 1
            p = p.next

        k %= n
        if k == 0:
            return head
        p = head
        for _ in range(n - k - 1):
            p = p.next

        q = p.next
        p.next = None
        p = q
        while p.next is not None:
            p = p.next
        p.next = head
        head = q
        return head
