/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return false
	}
	p := head
	q := head.Next
	for q != nil {
		p = p.Next
		q = q.Next
		if q == nil {
			return false
		}
		q = q.Next
		if q == p {
			return true
		}
	}
	return false
}
