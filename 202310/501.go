/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findMode(root *TreeNode) []int {
    cnt := make(map[int]int)

    var f func(p *TreeNode)
    f = func(p *TreeNode) {
        if p == nil {
            return
        }
        cnt[p.Val]++
        f(p.Left)
        f(p.Right)
    }

    f(root)
    var ans []int
    max_f := 0
    for _, v := range cnt {
        max_f = max(max_f, v)
    }
    for k, v := range cnt {
        if v == max_f {
            ans = append(ans, k)
        }
    }
    return ans
}
