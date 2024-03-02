import "slices"

func sortedSquares(nums []int) []int {
	n := len(nums)
	ans := make([]int, n)
	for i, a := range nums {
		ans[i] = a * a
	}
	slices.Sort(ans)
	return ans
}
