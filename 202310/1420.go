func numOfArrays(n int, m int, k int) int {
	mod := int(1e9 + 7)
	dp := make([][][]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([][]int, m+1)
		for j := 0; j <= m; j++ {
			dp[i][j] = make([]int, k+1)
			for l := 0; l <= k; l++ {
				dp[i][j][l] = -1
			}
		}
	}

	var f func(n, j, k int) int
	f = func(n, j, k int) int {
		if n == 0 {
			if k == 0 {
				return 1
			} else {
				return 0
			}
		}
		if k < 0 {
			return 0
		}
		if dp[n][j][k] != -1 {
			return dp[n][j][k]
		}
		ans := 0
		for i := 1; i <= j; i++ {
			ans = (ans + f(n-1, j, k)) % mod
		}
		for i := j + 1; i <= m; i++ {
			ans = (ans + f(n-1, i, k-1)) % mod
		}
		dp[n][j][k] = ans
		return ans
	}

	ans := 0
	for i := 1; i <= m; i++ {
		ans = (ans + f(n-1, i, k-1)) % mod
	}
	return ans
}
