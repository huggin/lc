func rob(nums []int) int {
	n := len(nums)
	if n == 1 {
		return nums[0]
	}
	dp := make([]int, n)
	dp[0] = nums[0]
	dp[1] = nums[1]
	for i := 2; i < n; i++ {
		dp[i] = dp[i-2] + nums[i]
		if i >= 3 {
			dp[i] = max(dp[i], dp[i-3]+nums[i])
		}
	}
	return max(dp[n-1], dp[n-2])
}
