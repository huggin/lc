func findDiagonalOrder(nums [][]int) []int {
	n := len(nums)
	var t [][]int
	for i := 0; i < n; i++ {
		for j := 0; j < len(nums[i]); j++ {
			if i+j == len(t) {
				t = append(t, []int{})
			}
			t[i+j] = append(t[i+j], nums[i][j])
		}
	}
	var ans []int
	for i := 0; i < len(t); i++ {
		for j := len(t[i]) - 1; j >= 0; j-- {
			ans = append(ans, t[i][j])
		}
	}
	return ans
}
