func kInversePairs(n int, k int) int {
	dp := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([]int, k+1)
		for j := 0; j <= k; j++ {
			dp[i][j] = -1
		}
	}
	const M = int(1e9 + 7)

	var f func(i, j int) int
	f = func(i, j int) int {
		if j == 0 {
			return 1
		}
		if j < 0 || i == 0 {
			return 0
		}
		if dp[i][j] != -1 {
			return dp[i][j]
		}
		dp[i][j] = ((f(i, j-1)+M-f(i-1, j-i))%M + f(i-1, j)) % M
		return dp[i][j]
	}
	return f(n, k)
}
