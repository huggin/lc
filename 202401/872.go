/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	l1 := make([]int, 0)
	l2 := make([]int, 0)

	var f func(p *TreeNode, leaf *[]int)
	f = func(p *TreeNode, leaf *[]int) {
		if p == nil {
			return
		}
		f(p.Left, leaf)
		if p.Left == nil && p.Right == nil {
			*leaf = append(*leaf, p.Val)
		}
		f(p.Right, leaf)
	}

	f(root1, &l1)
	f(root2, &l2)
	if len(l1) != len(l2) {
		return false
	}
	for k, p := range l1 {
		if p != l2[k] {
			return false
		}
	}
	return true
}
