/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeZeroSumSublists(head *ListNode) *ListNode {
	h := make(map[int]*ListNode)
	h[0] = nil
	p := head
	tot := 0
	s := []int{}
	for p != nil {
		tot += p.Val

		if q, ok := h[tot]; ok {
			for len(s) > 0 && h[s[len(s)-1]] != q {
				delete(h, s[len(s)-1])
				s = s[0 : len(s)-1]
			}
			if q == nil {
				head = p.Next
			} else {
				q.Next = p.Next
			}
		} else {
			h[tot] = p
			s = append(s, tot)
		}

		p = p.Next
	}
	return head
}
