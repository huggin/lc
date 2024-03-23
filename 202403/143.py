# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, p):
        prev = None
        while p:
            q = p.next
            p.next = prev
            prev = p
            p = q
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        
        p = head
        for _ in range(n // 2):
            p = p.next
        
        q = p.next
        p.next = None
        q = self.reverse(q)
        p = head

        while q is not None:
            pt = p.next
            pq = q.next
            p.next = q
            q.next = pt
            p = pt
            q = pq
        return head
