import "math"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func largestValues(root *TreeNode) []int {
	var ans []int
	if root == nil {
		return ans
	}
	var q []*TreeNode
	q = append(q, root)

	for len(q) > 0 {
		n := len(q)
		data := math.MinInt32
		for i := 0; i < n; i++ {
			curr := q[0]
			q = q[1:]
			data = max(data, curr.Val)
			if curr.Left != nil {
				q = append(q, curr.Left)
			}
			if curr.Right != nil {
				q = append(q, curr.Right)
			}
		}
		ans = append(ans, data)
	}
	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
