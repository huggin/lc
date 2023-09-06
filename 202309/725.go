/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func splitListToParts(head *ListNode, k int) []*ListNode {
	n := 0
	p := head
	for p != nil {
		n++
		p = p.Next
	}
	ave := n / k
	more := n % k
	p = head
	var ans []*ListNode
	var prev *ListNode = nil

	for i := 0; i < k; i++ {
		q := p
		ans = append(ans, q)
		for j := 0; j < ave; j++ {
			prev = p
			p = p.Next
		}
		if more > 0 {
			more--
			prev = p
			p = p.Next
		}
		if prev != nil {
			prev.Next = nil
		}
	}
	return ans
}
