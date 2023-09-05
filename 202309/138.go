/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
	m := make(map[*Node]*Node)
	m[nil] = nil
	var prevq *Node

	for p := head; p != nil; p = p.Next {
		q := new(Node)
		q.Val = p.Val
		if prevq != nil {
			prevq.Next = q
		}
		prevq = q
		m[p] = q
	}
	for p := head; p != nil; p = p.Next {
		m[p].Random = m[p.Random]
	}
	return m[head]
}
