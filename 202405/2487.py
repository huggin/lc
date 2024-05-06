# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = []
        while head:
            while len(s) > 0 and s[-1].val < head.val:
                s.pop()
            s.append(head)
            head = head.next

        ans = s[0]
        prev = s[0]
        for i in range(1, len(s)):
            prev.next = s[i]
            prev = s[i]
        prev.next = None
        return ans
