/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type Node struct {
	p *TreeNode
	l int
}

func isEvenOddTree(root *TreeNode) bool {
	var q []Node
	q = append(q, Node{root, 0})
	for len(q) > 0 {
		n := len(q)
		prev := 0
		if q[0].l%2 == 0 {
			prev = q[0].p.Val - 1
		} else {
			prev = q[0].p.Val + 1
		}
		for i := 0; i < n; i++ {
			curr := q[0]
			q = q[1:]
			if curr.l%2 == 0 {
				if curr.p.Val%2 == 0 || curr.p.Val <= prev {
					return false
				}
			} else {
				if curr.p.Val%2 == 1 || curr.p.Val >= prev {
					return false
				}
			}
			prev = curr.p.Val
			if curr.p.Left != nil {
				q = append(q, Node{curr.p.Left, curr.l + 1})
			}
			if curr.p.Right != nil {
				q = append(q, Node{curr.p.Right, curr.l + 1})
			}
		}
	}
	return true
}
