/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func construct(l, r int) []*TreeNode {
	if l > r {
		return []*TreeNode{nil}
	}
	var ans []*TreeNode
	for i := l; i <= r; i++ {
		left := construct(l, i-1)
		right := construct(i+1, r)
		for j := 0; j < len(left); j++ {
			for k := 0; k < len(right); k++ {
				root := new(TreeNode)
				root.Val = i
				root.Left = left[j]
				root.Right = right[k]
				ans = append(ans, root)
			}
		}
	}
	return ans
}

func generateTrees(n int) []*TreeNode {
	return construct(1, n)
}
