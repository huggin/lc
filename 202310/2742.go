func paintWalls(cost []int, time []int) int {
	n := len(cost)
	dp := make([]int, n+1)
	const oo = int(1e9)
	for i := 0; i <= n; i++ {
		dp[i] = oo
	}
	dp[0] = 0
	for i := 0; i < n; i++ {
		for j := n - 1; j >= 0; j-- {
			k := min(n, j+1+time[i])
			dp[k] = min(dp[k], dp[j]+cost[i])
		}
	}
	return dp[n]
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
