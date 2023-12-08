import "fmt"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func tree2str(root *TreeNode) string {
	var f func(p *TreeNode) string
	f = func(p *TreeNode) string {
		if p == nil {
			return ""
		}
		s := fmt.Sprintf("%d", p.Val)
		if p.Right != nil {
			if p.Left != nil {
				s += fmt.Sprintf("(%s)", f(p.Left))
			} else {
				s += "()"
			}
			s += fmt.Sprintf("(%s)", f(p.Right))
		} else {
			if p.Left != nil {
				s += fmt.Sprintf("(%s)", f(p.Left))
			}
		}
		return s
	}
	return f(root)
}
