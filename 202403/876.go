/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func middleNode(head *ListNode) *ListNode {
	p := head
	q := head
	for q != nil && q.Next != nil {
		p = p.Next
		q = q.Next.Next
	}
	return p
}
