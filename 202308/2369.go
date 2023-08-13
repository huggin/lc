func validPartition(nums []int) bool {
	n := len(nums)

	var dfs func(k int) bool

	dp := make([]int, n)
	for i := 0; i < n; i++ {
		dp[i] = -1
	}

	dfs = func(k int) bool {
		if k == n {
			return true
		}
		if dp[k] != -1 {
			return dp[k] == 1
		}
		var ans bool
		if k+1 < n && nums[k] == nums[k+1] {
			ans = ans || dfs(k+2)
			if k+2 < n && nums[k] == nums[k+2] {
				ans = ans || dfs(k+3)
			}
		} else if k+2 < n && nums[k]+1 == nums[k+1] && nums[k+1]+1 == nums[k+2] {
			ans = ans || dfs(k+3)
		}
		if ans {
			dp[k] = 1
		} else {
			dp[k] = 0
		}
		return ans
	}

	return dfs(0)
}
