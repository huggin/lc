func combinationSum4(nums []int, target int) int {
	dp := make([]int, target+1)
	dp[0] = 1
	for i := 0; i < target; i++ {
		for _, a := range nums {
			if i+a <= target {
				dp[i+a] += dp[i]
			}
		}
	}
	return dp[target]
}
