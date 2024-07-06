# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        prev = ans
        p = head
        while p:
            if p.val == 0:
                if p.next is not None:
                    prev.next = ListNode()
                prev = prev.next
            else:
                prev.val += p.val
            p = p.next

        return ans.next
