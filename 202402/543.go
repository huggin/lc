/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func diameterOfBinaryTree(root *TreeNode) int {
	ans := 0
	var f func(p *TreeNode) int
	f = func(p *TreeNode) int {
		if p == nil {
			return 0
		}
		left := f(p.Left)
		right := f(p.Right)
		ans = max(ans, left+right)
		return max(left, right) + 1
	}

	f(root)
	return ans
}
