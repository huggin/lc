# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        p = head
        n = 0
        while p:
            n += 1
            p = p.next

        p = head
        k2 = n - k
        while k > 1:
            k -= 1
            p = p.next

        q = head
        k = k2
        while k >= 1:
            k -= 1
            q = q.next

        temp = p.val
        p.val = q.val
        q.val = temp

        return head
