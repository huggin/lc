# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        i, j = 0, 0
        dir = ((0, 1), (1, 0), (0, -1), (-1, 0))
        d = 0

        ans = [([-1] * n) for _ in range(m)]
        while head:
            ans[i][j] = head.val
            head = head.next
            ni = i + dir[d][0]
            nj = j + dir[d][1]
            if ni >= m or nj >= n or ans[ni][nj] != -1:
                d = (d + 1) % 4
                ni = i + dir[d][0]
                nj = j + dir[d][1]
            i, j = ni, nj

        return ans
