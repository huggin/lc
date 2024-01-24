/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pseudoPalindromicPaths(root *TreeNode) int {
	var curr [9]int

	ans := 0
	var f func(p *TreeNode)
	f = func(p *TreeNode) {
		if p == nil {
			return
		}
		curr[p.Val-1]++
		if p.Left == nil && p.Right == nil {
			odd, even := 0, 0
			for i := 0; i < 9; i++ {
				if curr[i]%2 == 0 {
					even++
				} else {
					odd++
				}
			}
			if odd <= 1 {
				ans++
			}
		}
		f(p.Left)
		f(p.Right)
		curr[p.Val-1]--
	}

	f(root)
	return ans
}
