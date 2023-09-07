/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseBetween(head *ListNode, left int, right int) *ListNode {
	p := head
	var prev *ListNode
	for i := 0; i < left-1; i++ {
		prev = p
		p = p.Next
	}

	reverse := func(q *ListNode, n int) *ListNode {
		var prev *ListNode
		head := q
		for i := 0; i < n; i++ {
			next := q.Next
			q.Next = prev
			prev = q
			q = next
		}
		head.Next = q
		return prev
	}

	q := reverse(p, right-left+1)
	if prev != nil {
		prev.Next = q
	} else {
		head = q
	}
	return head
}   
