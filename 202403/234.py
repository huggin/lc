# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = []
        p = head
        while p:
            s.append(p.val)
            p = p.next

        p = head
        for d in reversed(s):
            if p.val != d:
                return False
            p = p.next

        return True
