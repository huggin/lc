# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        n = 0
        p = head
        while p:
            n += 1
            p = p.next

        a, b = divmod(n, k)
        p = head
        ans = []
        for _ in range(k):
            ans.append(p)
            q = p
            for _ in range(a):
                q = p
                p = p.next
            if b > 0:
                q = p
                p = p.next
                b -= 1
            if q is not None:
                q.next = None

        return ans
