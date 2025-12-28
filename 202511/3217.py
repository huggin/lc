# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        s = set(nums)

        head = ListNode(next=head)
        prev = head
        while prev.next:
            if prev.next.val in s:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return head.next
