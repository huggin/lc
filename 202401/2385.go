/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type Node struct {
	node  *TreeNode
	depth int
}

func amountOfTime(root *TreeNode, start int) int {
	ans := 0
	var f func(p *TreeNode) (int, bool)
	f = func(p *TreeNode) (int, bool) {
		if p == nil {
			return 0, false
		}

		if p.Val == start {
			q := make([]Node, 0)
			q = append(q, Node{p, 0})
			depth := 0
			for len(q) > 0 {
				curr := q[0]
				q = q[1:]
				depth = max(depth, curr.depth)
				if curr.node.Left != nil {
					q = append(q, Node{curr.node.Left, curr.depth + 1})
				}
				if curr.node.Right != nil {
					q = append(q, Node{curr.node.Right, curr.depth + 1})
				}
			}
			ans = max(ans, depth)
			return 0, true
		}
		left, fl := f(p.Left)
		right, fr := f(p.Right)
		if fl || fr {
			ans = max(ans, left+right+1)
			if fl {
				return left + 1, true
			} else {
				return right + 1, true
			}
		}

		return max(left, right) + 1, false
	}
	f(root)

	return ans
}
