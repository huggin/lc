func findPaths(m int, n int, maxMove int, startRow int, startColumn int) int {
	var dp [50][50][51]int
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			for k := 0; k <= maxMove; k++ {
				dp[i][j][k] = -1
			}
		}
	}
	dx := [4]int{-1, 0, 0, 1}
	dy := [4]int{0, -1, 1, 0}
	const M = int(1e9 + 7)

	var f func(i, j, k int) int
	f = func(i, j, k int) int {
		if i < 0 || i >= m || j < 0 || j >= n {
			return 1
		}
		if k == 0 {
			return 0
		}
		if dp[i][j][k] != -1 {
			return dp[i][j][k]
		}
		ans := 0
		for l := 0; l < 4; l++ {
			ans = (ans + f(i+dx[l], j+dy[l], k-1)) % M
		}
		dp[i][j][k] = ans
		return ans
	}
	return f(startRow, startColumn, maxMove)
}
