func numRollsToTarget(n int, k int, target int) int {
	dp := make([][]int, target+1)
	for i := 0; i <= target; i++ {
		dp[i] = make([]int, n+1)
		for j := 0; j <= n; j++ {
			dp[i][j] = -1
		}
	}
	const M = int(1e9 + 7)

	var f func(i, j int) int
	f = func(i int, j int) int {
		if i < 0 || j < 0 || i > j*k {
			return 0
		}
		if j == 0 && i == 0 {
			return 1
		}

		if dp[i][j] != -1 {
			return dp[i][j]
		}
		ans := 0
		for ii := 1; ii <= k; ii++ {
			ans = (ans + f(i-ii, j-1)) % M
		}
		dp[i][j] = ans
		return ans
	}

	return f(target, n)
}
