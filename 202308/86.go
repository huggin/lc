/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func partition(head *ListNode, x int) *ListNode {
	p := head
	var small, big, sp, bp *ListNode
	for p != nil {
		next := p.Next
		if p.Val < x {
			if small == nil {
				small = p
			} else {
				sp.Next = p
			}
			sp = p
		} else {
			if big == nil {
				big = p
			} else {
				bp.Next = p
			}
			bp = p
		}
		p = next
	}
	if bp != nil {
		bp.Next = nil
	}
	if sp == nil {
		return big
	} else {
		sp.Next = big
	}
	return small
}
