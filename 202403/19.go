/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	p := head
	q := p
	for i := 0; i < n; i++ {
		q = q.Next
	}
	if q == nil {
		return head.Next
	}
	for {
		if q.Next == nil {
			p.Next = p.Next.Next
			break
		}
		q = q.Next
		p = p.Next
	}
	return head
}
