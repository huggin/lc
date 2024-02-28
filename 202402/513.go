/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findBottomLeftValue(root *TreeNode) int {
	ans := -1
	level := -1

	var f func(p *TreeNode, curr int)
	f = func(p *TreeNode, curr int) {
		if p == nil {
			return
		}
		if p.Left == nil && p.Right == nil && curr > level {
			level = curr
			ans = p.Val
		}
		f(p.Left, curr+1)
		f(p.Right, curr+1)
	}

	f(root, 0)
	return ans
}
