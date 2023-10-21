func push(q []int, dp []int, i int) []int {
	for len(q) > 0 && dp[q[len(q)-1]] < dp[i] {
		q = q[0 : len(q)-1]
	}
	q = append(q, i)
	return q
}

func constrainedSubsetSum(nums []int, k int) int {
	n := len(nums)
	var q []int
	dp := make([]int, n)
	dp[0] = nums[0]
	ans := dp[0]
	q = push(q, nums, 0)

	for i := 1; i < n; i++ {
		dp[i] = max(nums[i], nums[i]+dp[q[0]])
		ans = max(ans, dp[i])
		if i-k >= 0 && len(q) > 0 && dp[i-k] == dp[q[0]] {
			q = q[1:]
		}
		q = push(q, dp, i)

	}
	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
