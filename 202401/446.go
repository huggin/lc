func numberOfArithmeticSlices(nums []int) int {
	n := len(nums)
	ans := 0
	dp := make([]map[int]int, n)

	var f func(d int, k int) int
	f = func(d int, k int) int {
		if len(dp[k]) > 0 {
			if v, ok := dp[k][d]; ok {
				return v
			}
		} else {
			dp[k] = make(map[int]int)
		}
		ans := 1
		for i := k + 1; i < n; i++ {
			if nums[i]-nums[k] == d {
				ans += f(d, i)
			}
		}
		dp[k][d] = ans
		return ans
	}

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			d := nums[j] - nums[i]
			for k := j + 1; k < n; k++ {
				if nums[k]-nums[j] == d {
					ans += f(d, k)
				}
			}
		}
	}
	return ans
}
