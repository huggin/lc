func rearrangeArray(nums []int) []int {
	n := len(nums)
	ans := make([]int, n)
	i, j := 0, 1
	for _, a := range nums {
		if a > 0 {
			ans[i] = a
			i += 2
		} else {
			ans[j] = a
			j += 2
		}
	}
	return ans
}
