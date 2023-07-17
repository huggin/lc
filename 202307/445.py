# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def reverse(p):
            prev = None
            while p:
                n = p.next
                p.next = prev
                prev = p
                p = n
            return prev

        l1 = reverse(l1)
        l2 = reverse(l2)
        ans = None
        prev = None
        more = 0
        while l1 and l2:
            d = l1.val + l2.val + more
            if d >= 10:
                d -= 10
                more = 1
            else:
                more = 0
            if ans is None:
                ans = ListNode(d)
                prev = ans
            else:
                prev.next = ListNode(d)
                prev = prev.next
            l1 = l1.next
            l2 = l2.next

        p = l1
        if l1 is None:
            p = l2
        if p is None:
            if more == 1:
                prev.next = ListNode(1)
        else:
            prev.next = p
            prev = p
            while p:
                p.val += more
                if p.val >= 10:
                    p.val -= 10
                    more = 1
                else:
                    more = 0
                prev = p
                p = p.next

            if more == 1:
                prev.next = ListNode(1)

        return reverse(ans)
