/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rangeSumBST(root *TreeNode, low int, high int) int {
	ans := 0
	var f func(p *TreeNode)
	f = func(p *TreeNode) {
		if p == nil {
			return
		}
		if low <= p.Val && p.Val <= high {
			ans += p.Val
		}
		f(p.Left)
		f(p.Right)
	}
	f(root)
	return ans
}
