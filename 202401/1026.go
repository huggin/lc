/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxAncestorDiff(root *TreeNode) int {
	ans := 0
	var f func(p *TreeNode, mi, ma int)
	f = func(p *TreeNode, mi, ma int) {
		if p == nil {
			return
		}
		ans = max(ans, abs(p.Val-mi))
		ans = max(ans, abs(p.Val-ma))
		f(p.Left, min(mi, p.Val), max(ma, p.Val))
		f(p.Right, min(mi, p.Val), max(ma, p.Val))
	}

	f(root, root.Val, root.Val)
	return ans
}

func abs(a int) int {
	if a >= 0 {
		return a
	}
	return -a
}
