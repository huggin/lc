# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(p):
            prev = None
            while p:
                n = p.next
                p.next = prev
                prev = p
                p = n
            return prev

        p = reverse(head)

        more = 0
        ans = p
        while p:
            p.val = p.val + p.val + more
            if p.val >= 10:
                p.val -= 10
                more = 1
            else:
                more = 0
            prev = p
            p = p.next

        if more == 1:
            prev.next = ListNode(more)

        return reverse(ans)
