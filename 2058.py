# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cc = []
        i = 0
        p = head
        while p:
            q = p.next
            if q and q.next:
                if p.val < q.val and q.val > q.next.val or p.val > q.val and q.val < q.next.val:
                    cc.append(i)
            i += 1
            p = q
        
        if len(cc) >= 2:
            return [min(cc[i+1] - cc[i] for i in range(len(cc)-1)), cc[-1] - cc[0]]
        return [-1, -1]
