/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func inorderTraversal(root *TreeNode) []int {
	var ans []int

	var f func(p *TreeNode)
	f = func(p *TreeNode) {
		if p == nil {
			return
		}
		f(p.Left)
		ans = append(ans, p.Val)
		f(p.Right)
	}

	f(root)
	return ans
}
