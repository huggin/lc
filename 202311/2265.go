/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func averageOfSubtree(root *TreeNode) int {
    ans := 0
    var f func(p *TreeNode) (int, int)
    f = func(p *TreeNode) (int, int){
        if p == nil {
            return 0, 0
        }
        ls, lc := f(p.Left)
        rs, rc := f(p.Right)
        if (ls + rs + p.Val) / (lc + rc + 1) == p.Val {
            ans++
        }
        return ls + rs + p.Val, lc + rc + 1
    }

    f(root)
    return ans
}
